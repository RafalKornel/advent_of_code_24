from main import solution_1, solution_2


test_input = [
    ([7, 6, 4, 2, 1], True, True),
    ([1, 2, 7, 8, 9], False, False),
    ([9, 7, 6, 2, 1], False, False),
    ([1, 3, 2, 4, 5], False, True),
    ([8, 6, 4, 4, 1], False, True),
    ([1, 3, 6, 7, 9], True, True),
    ([1, 1, 1, 1, 1], False, False),
    ([45, 48, 51, 52, 55, 58, 60, 60], False, True),
    ([31, 34, 34, 36, 37, 37], False, False),
    ([11, 8, 11, 12, 13, 14, 17], False, True),
]


def test_1():
    inp = [line[0] for line in test_input]
    expected = [line[1] for line in test_input]

    result, _ = solution_1(inp)

    assert expected == result, f"Expected {expected}, but got {result}"


def test_2():
    inp = [line[0] for line in test_input]
    expected = [line[2] for line in test_input]

    result, _ = solution_2(inp)

    assert expected == result, f"Expected {expected}, but got {result}"


if __name__ == "__main__":
    test_1()
    test_2()

    print("All tests passed!")
