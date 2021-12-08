from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Iterable, Iterator

from aoc import cache


@dataclass
class Board:
    _numbers: List[List[Optional[int]]]
    _row_marks: List[int] = field(init=False)
    _col_marks: List[int] = field(init=False)

    def __post_init__(self):
        self._row_marks = [0] * 5
        self._col_marks = [0] * 5

    def score(self) -> Optional[int]:
        """ Returns False when the board has not won, returns score otherwise. """
        won = False
        for row_mark_count in self._row_marks:
            if row_mark_count == 5:
                won = True
                break
        for col_mark_count in self._col_marks:
            if won == True or col_mark_count == 5:
                won = True
                break
        if not won:
            return None
        score = 0
        for line in self._numbers:
            for col in line:
                if col is not None:
                    score += col
        return score

    def mark(self, val: int):
        for y, line in enumerate(self._numbers):
            for x, col in enumerate(line):
                if self._numbers[y][x] == val:
                    self._numbers[y][x] = None
                    self._row_marks[y] += 1
                    self._col_marks[x] += 1
                    return


def boards_from_lines(lines: Iterator[str]) -> Iterable[Board]:
    try:
        while True:
            next(lines)
            numbers = []
            for i in range(5):
                line = next(lines).replace('  ', ' ').split(' ')
                row = [int(s) for s in line]
                numbers.append(row)
            yield Board(numbers)
    except StopIteration:
        pass


def read_input() -> Tuple[List[int], List[Board]]:
    lines = cache.input_for_day(4).lines()
    pulls = [int(i) for i in next(lines).split(',')]
    boards = [board for board in boards_from_lines(lines)]
    return pulls, boards


def run() -> int:
    pulls, boards = read_input()
    for pull in pulls:
        for board in boards:
            board.mark(pull)
            score = board.score()
            if score is not None:
                return score * pull


if __name__ == "__main__":
    print(run())
