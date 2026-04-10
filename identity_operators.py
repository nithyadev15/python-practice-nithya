# Identity operators are used to compare two objects, not if they are equal but if they are the same objects in the same memory location.

def identity():
    # Is example
    a = 10
    b = 10
    print(a is b)

    # Different objects with the same value
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a is b)
    # Eventhough the elements are same, lists are stored in seperate locations.

    # compare identity vs equality
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a==b)
    print(a is b)

    # Using is not
    a = [1, 2]
    b = [1, 2]
    print(a is not b)

    # Assigning the same reference
    a = [1, 2]
    b = a
    print(a is b)

    # Checking None
    x = None
    if x is None:
        print("x is empty")

    # Identity with functions
    def func():
        return [1, 2]
    a = func()
    b = func()
    print(a is b)
