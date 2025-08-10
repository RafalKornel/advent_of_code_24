from pathlib import Path


def parse_input():
    with open(Path(__file__).parent.as_posix() + "/" + "input.txt", "r") as file:
        lines = file.readlines()

        levels = [[int(v) for v in line.split()] for line in lines]

        return levels


def validate_level(level: list[int]):
    first = level[0]
    second = level[1]

    if not first or not second:
        return True, None

    initial_direction = 1 if second > first else -1

    for index in range(len(level) - 1):
        first = level[index]
        second = level[index + 1]

        current_dir = 1 if second > first else -1

        if current_dir is not initial_direction:
            return False, index

        jump = abs(first - second)

        if (jump < 1) or (jump > 3):
            return False, index

    return True, None


def solution_1(levels: list[list[int]]) -> tuple[list[bool], bool]:
    valid_num = len(levels)
    report_result = [True for _ in levels]

    for i, level in enumerate(levels):
        result, idx = validate_level(level)

        report_result[i] = result

        if result is False:
            valid_num -= 1

    return report_result, valid_num


def solution_2(levels: list[list[int]]) -> tuple[list[bool], bool]:
    valid_num = len(levels)
    report_result = [True for _ in levels]

    for i, level in enumerate(levels):
        result, idx = validate_level(level)

        if result is True:
            report_result[i] = result

            continue

        left = level.copy()
        left.pop(idx - 1)

        left_result, _idx = validate_level(left)

        if left_result is True:
            report_result[i] = left_result

            continue

        center = level.copy()
        center.pop(idx)

        center_result, _idx = validate_level(center)

        if center_result is True:
            report_result[i] = center_result

            continue

        right = level.copy()
        right.pop(idx + 1)

        right_result, _idx = validate_level(right)

        if right_result is True:
            report_result[i] = right_result

            continue

        report_result[i] = False
        valid_num -= 1

    return report_result, valid_num


if __name__ == "__main__":
    inp = parse_input()

    valid_levels_1, num_of_valid_levels_1 = solution_1(inp)

    print(f"[1] Number of valid levels: {num_of_valid_levels_1}")

    valid_levels_2, num_of_valid_levels_2 = solution_2(inp)

    print(f"[2] Number of valid levels: {num_of_valid_levels_2}")
