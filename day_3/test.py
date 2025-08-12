from main import solution_1, solution_2


test_input_1 = "mul(7,8)xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(1,2)"
test_input_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))mul(1,2)"

# test_input = "mul(1,2)xmul(3,4)"


def test_1():
    total= solution_1(test_input_1)

    expected = 163 + 56

    assert total == expected, f"Failed! Total: {total}"

    print(total)

def test_2():
    total, operations = solution_2(test_input_2)

    expected = 50

    assert total == expected, f"Failed! Total: {total}, Operations: {operations}"

    print(total, operations)    


if __name__ == "__main__":
    test_1()
    test_2()

    print("Tests passed!")
