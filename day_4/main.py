from pathlib import Path


def parse_input() -> list[str]:
    with open(Path(__file__).parent.as_posix() + "/" + "input.txt", "r") as file:
        return file.read().split("\n")


def count_in_diag(row: str, is_reverse: bool = False, word="XMAS") -> int:
    search = row[::-1] if is_reverse else row

    count = 0

    if len(search) == len(word):
        return search == word

    for i in range(0, len(search) - len(word) + 1):
        s = search[i : i + len(word)]
        if s == word:
            count += 1

    return count


def get_diagonals(board: list[str]):
    diag = []

    size = len(board[0])

    for j in range(size):
        curr_row_right = ""
        curr_row_left = ""

        for i in range(0, len(board)):
            curr_row_right += board[i][(i + j) % size]
            curr_row_left += board[i][(j - i + size) % size]

        s1, s2 = curr_row_right[: size - j], curr_row_right[size - j :]
        s3, s4 = curr_row_left[: j + 1], curr_row_left[j + 1 :]

        diag.append(s1)
        diag.append(s2)
        diag.append(s3)
        diag.append(s4)

    return [el for el in diag if el != ""]


def solution_1(board: list[str]) -> int:
    if len(board) == 0:
        return 0

    size = len(board[0])

    rows = [b for b in board]
    cols = ["".join([board[i][j] for i in range(len(board))]) for j in range(size)]
    diag = get_diagonals(board)

    in_rows = 0
    in_rows_reverse = 0
    in_cols = 0
    in_cols_reverse = 0
    in_diag = 0
    in_diag_reverse = 0

    total = 0

    for r in rows:
        in_rows += count_in_diag(r)

        in_rows_reverse += count_in_diag(r, True)

    for c in cols:
        in_cols += count_in_diag(c)
        in_cols_reverse += count_in_diag(c, True)

    for d in diag:
        in_diag += count_in_diag(d)
        in_diag_reverse += count_in_diag(d, True)

    print("len", len(board))
    print("size", size)

    return (
        in_rows
        + in_rows_reverse
        + in_cols
        + in_cols_reverse
        + in_diag
        + in_diag_reverse
    )


def solution_2(board: list[str]) -> int:
    rows = len(board)

    total = 0

    word = "mas"

    if rows < 3:
        return 0

    cols = len(board[0])

    if cols < 3:
        return 0

    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            d1 = "".join([board[y - 1][x - 1], board[y][x], board[y + 1][x + 1]]).lower()
            d2 = "".join([board[y + 1][x - 1], board[y][x], board[y - 1][x + 1]]).lower()

            is_d1_correct = d1 == word or d1 == word[::-1]
            is_d2_correct = d2 == word or d2 == word[::-1]

            if is_d1_correct and is_d2_correct:
                total += 1
            

    return total

if __name__ == "__main__":
    board = parse_input()

    count_1 = solution_1(board)

    print(f"Solution 1: {count_1}")

    count_2 = solution_2(board)

    print(f"Solution 2: {count_2}")
