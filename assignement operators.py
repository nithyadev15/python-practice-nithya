# assignment operators - These are used to assign values to variables

def test_assignment_operator():
    # assignment
    number = 5
    assert number == 5

    # multiple assignment
    first_variable, second_variable = 0, 1
    assert first_variable == 0
    assert second_variable == 1 

def test_augmented_assignment_operator():
    # assignment operators combined with arithmetic and bitwise operators

    # assignment: +=
    number = 3
    number += 5
    assert number == 8

    # assignment: -=
    number = 8
    number -= 3
    assert number == 5

    # assignment: *=
    number = 5
    number *= 3
    assert number == 15

    # assignment: /=
    number = 8
    number /= 4
    assert number == 2