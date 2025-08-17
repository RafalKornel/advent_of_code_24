from main import solution_1, solution_2

test_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def test_1():
    res = solution_1(test_input.split("\n")[1::])

    expected = 18

    assert res == expected, f"Expected {expected} got {res}"

def test_2():
    res = solution_2(test_input.split("\n")[1::])

    expected = 9

    assert res == expected, f"Expected {expected} got {res}"
  
if __name__ == "__main__":
    test_1()
    test_2()

    print("All tests passed!")