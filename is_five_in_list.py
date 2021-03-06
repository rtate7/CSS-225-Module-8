# Robert Tate
# 3/6/2021

# print_list_if_it_contains_5 takes a list as its input and prints the list
# if the value 5 is in that list

def print_list_if_it_contains_5(list):
    if 5 in list:
        print(list)

example_list_1 = [1, 2, 3, 4, 5]
print_list_if_it_contains_5(example_list_1)

example_list_2 = [2, 2, 3, 4, 9]
print_list_if_it_contains_5(example_list_2)


