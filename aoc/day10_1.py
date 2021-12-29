from typing import Tuple, List, Optional

from aoc import cache

BRACKET_MAP = {
    "{": "}",
    "[": "]",
    "<": ">",
    "(": ")"
}

BRACKET_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def parse_one(line: str) -> Tuple[Optional[str], List[str]]:
    """
    Returns (first corruption char, remaining stack)
    """
    stack = []
    for c in line:
        if c in BRACKET_MAP.keys():
            stack.append(c)
            continue
        expected = BRACKET_MAP[stack[-1]]
        if c != expected:
            return c, stack
        stack.pop()
    return None, stack


def solve() -> int:
    total = 0
    for line in cache.input_for_day(10).lines():
        corrupted_char, _ = parse_one(line)
        if corrupted_char:
            total += BRACKET_SCORE[corrupted_char]
    return total


if __name__ == "__main__":
    print(solve())
