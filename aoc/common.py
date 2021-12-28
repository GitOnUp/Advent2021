from dataclasses import dataclass
from logging import Logger
from pathlib import Path
from typing import Iterable

_REMOTE_FORMAT: str = "https://adventofcode.com/2021/day/{}/input"


class Logged(type):
    def __new__(mcs, name, bases, dct):
        x = super().__new__(mcs, name, bases, dct)
        x.logger = Logger(name)
        return x


@dataclass
class InputCache(metaclass=Logged):
    path: Path

    def _ensure_path(self) -> None:
        if not self.path.exists():
            self.logger.debug(f"Creating cache path: {self.path}")
            self.path.mkdir()
            return

        if not self.path.is_dir():
            raise ValueError(f"Provided cache location ('{self.path}') is not a directory")
        self.logger.debug(f"Using existing cache path: {self.path}")

    @staticmethod
    def default() -> "InputCache":
        return InputCache(Path.home() / '.aoc21')

    def input_for_day(self, day: int) -> "InputFile":
        self._ensure_path()
        day_path = self.path / f"{day}.txt"
        if not day_path.exists():
            raise ValueError(f"Input for day {day} does not exist in {self.path}; download it first")
        return InputFile(day_path)


@dataclass
class InputFile(metaclass=Logged):
    path: Path

    def lines(self) -> Iterable[str]:
        with open(self.path, 'r') as f:
            for line in f:
                yield line.strip()


__all__ = [
    "InputCache",
    "InputFile",
    "Logged"
]