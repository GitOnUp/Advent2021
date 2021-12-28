import os
import requests

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

    def download_for_day(self, day: int, target_path: Path) -> None:
        cookies_file_str = os.environ.get("COOKIES_FILE", None)
        if cookies_file_str is None:
            raise ValueError(f"Input for day {day} does not exist in {self.path}; download it first, or provide "
                             f"cookies for the advent of code site in a text file pointed at by the COOKIES_FILE "
                             f"environment variable.")
        cookies_path = Path(cookies_file_str).resolve()
        if not cookies_path.exists() or not cookies_path.is_file():
            raise ValueError(f"COOKIES_FILE ({str(cookies_path)}) does not exist or is not a file.")
        cookies = {}
        with open(cookies_path, "r") as cookies_file:
            for line in cookies_file:
                cookie_line = line.strip().split("=")
                if len(cookie_line) != 2:
                    raise ValueError("Expected cookies file format to be 'cookie_name=cookie_value', separated by "
                                     "newline.")
                cookie_name, cookie_value = cookie_line
                cookies[cookie_name] = cookie_value
        day_response = requests.get(_REMOTE_FORMAT.format(day), cookies=cookies)
        if day_response.status_code != 200:
            raise ValueError(f"Got status code {day_response.status_code} while downloading day {day}: "
                             f"{day_response.text}")
        with open(target_path, 'w') as target_file:
            target_file.writelines(day_response.text)

    def input_for_day(self, day: int) -> "InputFile":
        self._ensure_path()
        day_path = self.path / f"{day}.txt"
        if not day_path.exists():
            self.download_for_day(day, day_path)
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