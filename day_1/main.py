from pathlib import Path


def parse_input():

    with open(Path(__file__).parent.as_posix() + "/" + "input.txt", "r") as file:
        lines = file.readlines()

        tuples = [line.split() for line in lines]

        left = []
        right = []

        for left_side, right_side in tuples:
            left.append(int(left_side))
            right.append(int(right_side))

        return left, right


def solution_1(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()

    distances = []

    for i in range(len(left)):
        distances.append(abs(left[i] - right[i]))

    return sum(distances)


def solution_2(left: list[int], right: list[int]) -> int:
    right_occurances = {}

    for r in right:
        if r in right_occurances:
            right_occurances[r] += 1
        else:
            right_occurances[r] = 1

    total = 0

    for l in left:
        if l not in right_occurances:
            continue

        occurances = right_occurances[l]

        total += occurances * l

    return total


if __name__ == "__main__":
    inp = parse_input()

    result_1 = solution_1(inp[0], inp[1])

    print(f"Result for solution 1: {result_1}")

    result_2 = solution_2(inp[0], inp[1])

    print(f"Result for solution 2: {result_2}")
