# Robert Tate
# 3/6/2021

# is_leap_year is a function that takes a year as a parameter and returns True if the 
# year is a leap year and False if it is not.
# is_leap_year_ui implements is_leap_year for testing and demonstration.

def is_leap_year(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

def is_leap_year_ui():
    year = int(input("Please enter a year for which you'd like the leaposity checked: "))
    if is_leap_year(year):
        is_or_is_not = "is"
    else:
        is_or_is_not = "is not"
    print(f"{year} {is_or_is_not} a leap year.")

is_leap_year_ui()

