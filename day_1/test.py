from main import solution_1, solution_2

left = [3, 4, 2, 1, 3, 3]
right = [4, 3, 5, 3, 9, 3]


def test_1():
    expected = 11

    result = solution_1(left, right)

    assert result == expected, f"Expected {expected}, but got {result}"


def test_2():
    expected = 31

    result = solution_2(left, right)

    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    test_1()
    test_2()
    print("All tests passed!")
