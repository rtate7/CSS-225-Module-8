# Robert Tate
# 3/6/2021

# is_equal takes two inputs and returns a string which describes 
# whether the numbers are equal.
# is_equal_ui manages the user interface and calls is_equal

def is_equal_ui():
    value1 = input("Enter the first value: ")
    value2 = input("Enter the second value: ")
    print(is_equal(value1, value2))

def is_equal(a, b):
    is_or_is_not = "is" if a == b else "is not"
    return f"{a} {is_or_is_not} equal to {b}."

is_equal_ui()

