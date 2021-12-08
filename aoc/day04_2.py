from aoc.day04_1 import read_input


def run():
    pulls, boards = read_input()
    winner = [False] * len(boards)
    remaining = len(boards) - 1
    for pull in pulls:
        for boardnum, board in enumerate(boards):
            if winner[boardnum]:
                continue
            board.mark(pull)
            score = board.score()
            if score is not None:
                if remaining == 0:
                    return board.score() * pull
                else:
                    winner[boardnum] = True
                    remaining -= 1


if __name__ == "__main__":
    print(run())
