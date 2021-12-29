from aoc import cache
from aoc.day10_1 import parse_one, BRACKET_MAP

INCOMPLETE_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def solve() -> int:
    scores = []
    for line in cache.input_for_day(10).lines():
        corrupted_char, stack = parse_one(line)
        if corrupted_char:
            continue
        score = 0
        for c in reversed(stack):
            score = (score * 5) + INCOMPLETE_SCORES[BRACKET_MAP[c]]
        scores.append(score)
    scores = sorted(scores)
    return scores[len(scores) // 2]


if __name__ == "__main__":
    print(solve())
