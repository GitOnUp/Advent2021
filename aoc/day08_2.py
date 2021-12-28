from itertools import permutations
from typing import List, Mapping, Optional

from aoc.day08_1 import parse


def segments_to_bits(segment_str: str) -> int:
    value = 0
    for segment in segment_str:
        bit = ord(segment) - ord('a')
        value |= 1 << bit
    return value


def generate_segment_map() -> Mapping[int, int]:
    mapping: Mapping[str, int] = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9
    }
    return {segments_to_bits(key): value for key, value in mapping.items()}


segment_bits_to_number: Mapping[int, int] = generate_segment_map()


def translate(permutation: List[str], segments: str) -> Optional[int]:
    mapping = {ord(key): ord(value) for key, value in zip(permutation, list("abcdefg"))}
    translated = segments.translate(mapping)
    bits = segments_to_bits(translated)
    return segment_bits_to_number.get(bits)


def solve_one(tests: List[str], values: List[str]) -> int:
    """ Solves, but in a very brute-force way since it's still fast """
    for assignments in permutations("abcdefg"):
        remaining_numbers = set(range(0, 10))
        for test_segments in tests:
            translated = translate(assignments, test_segments)
            if translated is None:
                break
            try:
                remaining_numbers.remove(translated)
            except KeyError:
                break

        if len(remaining_numbers) > 0:
            continue

        output = 0
        for ix, value in enumerate(values):
            translated = translate(assignments, value)
            output += translated * (10 ** (3 - ix))
        return output


if __name__ == "__main__":
    total = 0
    for tests, values in parse():
        total += solve_one(tests, values)
    print(total)

