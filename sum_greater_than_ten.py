# Robert Tate
# 3/6/2021

# sum_greater_than_10 takes two inputs and returns a string which describes 
# whether the sum of the numbers is greater tahn, less than, or equal
# to ten.
# sum_greater_than_10_ui manages the user interface and calls sum_greater_than_10

def sum_greater_than_10(num1, num2):
    sum = num1 + num2
    if sum > 10:
        relationship = "greater than"
    elif sum < 10:
        relationship = "less than"
    else:
        relationship = "equal to"
    return f"{num1} plus {num2} is {relationship} 10."

def sum_greater_than_10_ui():
    value1 = int(input("Enter the first value: "))
    value2 = int(input("Enter the second value: "))
    print(sum_greater_than_10(value1, value2))

sum_greater_than_10_ui()


