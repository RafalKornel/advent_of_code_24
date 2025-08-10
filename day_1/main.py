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

    total = 0

    for i in range(len(left)):
        total += abs(left[i] - right[i])


    return total

def solution_2(left: list[int], right: list[int]) -> int:
    right_occurances = {}

    # Create map of occurances - O(n)
    for r in right:
        if r in right_occurances:
            right_occurances[r] += 1
        else:
            right_occurances[r] = 1

    total = 0

    # calculate total score - O(n)
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
