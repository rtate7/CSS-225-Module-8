# Robert Tate
# 3/6/2021

# character_status is a function that accepts four argurments: character_items,
# required_items, character_debuffs, and forbidden_debuffs and returns a boolean
# value which represents whether the character can perform a task based on whether 
# the character has all required items and whether the character has any of the 
# forbidden debuffs.
# 
# The second, object-oriented implementation requires the character and the task
# to be instantiated as objects. I added this second implementation as a personal 
# exercise and found that it was much easier to debug as I made tweaks and changes. 
# Also, I think the object-oriented code is much more readable, provided that the 
# reader is familiar with the Python syntax and OO concepts. 

import os 
os.system('cls' if os.name == 'nt' else 'clear')

# test values for use in both approaches
bob_items = ["rope", "coat", "first aid kit", "pan", "Mittens of Bernie", "pen", "paper", "idea"]
bob_debuffs = ["distraction", "confusion"]
climb_mountain_required_items = ["rope", "coat", "first aid kit"]
climb_mountain_forbidden_debuffs = ["slow"]
cook_a_meal_required_items = ["pan", "groceries"]
cook_a_meal_forbidden_debuffs = ["small"]
write_a_book_required_items = ["pen", "paper", "idea"]
write_a_book_forbidden_debuffs = ["confusion"]

# Simpler functional approach
def character_status(character_items, required_items, character_debuffs, forbidden_debuffs):
    all_conditions_met = True
    for item in required_items:
        if item in character_items:
            print(f"Character has required item: {item}")
        else:
            all_conditions_met = False
            print(f"Character does not have required item: {item}")
    for debuff in forbidden_debuffs:
        if debuff in character_debuffs:
            print(f"Character has forbidden debuff: {debuff}")
            all_conditions_met = False
        else:
            print(f"Character does not have forbidden debuff: {debuff}")
    return all_conditions_met

def function_show_character_ability_to_perform_task(character_name, task_name, character_items, required_items, character_debuffs, forbidden_debuffs):
    if character_status(character_items, required_items, character_debuffs, forbidden_debuffs):
        can_or_can_not = "can"
    else:
        can_or_can_not = "can not"
    print (f"{character_name} {can_or_can_not} {task_name}.\n")


print("Using the simple function approach:\n")

function_show_character_ability_to_perform_task("Bob", "climb a mountain", 
    bob_items, climb_mountain_required_items, bob_debuffs, climb_mountain_forbidden_debuffs)

function_show_character_ability_to_perform_task("Bob", "cook a meal", 
    bob_items, cook_a_meal_required_items, bob_debuffs, cook_a_meal_forbidden_debuffs)

function_show_character_ability_to_perform_task("Bob", "write a book", 
    bob_items, write_a_book_required_items, bob_debuffs, write_a_book_forbidden_debuffs)

#-----------------------------------------------------------------------------------------

# Cleaner, more extensible, object-oriented approach:

class Character:
    def __init__(self, name):
        self.name = name

    def set_items(self, items):
        self.items = items

    def set_debuffs(self, debuffs):
        self.debuffs = debuffs

    def can_perform(self, task):
        all_conditions_met = True
        for item in task.required_items:
            if item in self.items:
                print(f"{self.name} has required item: {item}")
            else:
                all_conditions_met = False
                print(f"{self.name} does not have required item: {item}")
        for debuff in task.forbidden_debuffs:
            if debuff in self.debuffs:
                print(f"{self.name} has forbidden debuff: {debuff}")
                all_conditions_met = False
            else:
                print(f"{self.name} does not have forbidden debuff: {debuff}")
        return all_conditions_met

class Task:
    def __init__(self, name):
        self.name = name

    def set_required_items(self, items):
        self.required_items = items

    def set_forbidden_debuffs(self, debuffs):
        self.forbidden_debuffs = debuffs

def oo_show_character_ability_to_perform_task(character, task):
    if character.can_perform(task):
        can_or_can_not = "can"
    else:
        can_or_can_not = "can not"
    print (f"{character.name} {can_or_can_not} {task.name}.\n")

print("---------------------------------------\n")
print("Using the Object-Oriented approach:\n")

# instantiate objects and set their field data:
bob = Character("Bob")
bob.set_items(bob_items)
bob.set_debuffs(bob_debuffs)

climb_mountain = Task("climb a mountain")
climb_mountain.set_required_items(climb_mountain_required_items)
climb_mountain.set_forbidden_debuffs(climb_mountain_forbidden_debuffs)

cook_a_meal = Task("cook a meal")
cook_a_meal.set_required_items(cook_a_meal_required_items)
cook_a_meal.set_forbidden_debuffs(cook_a_meal_forbidden_debuffs)

write_a_book = Task("write a book")
write_a_book.set_required_items(write_a_book_required_items)
write_a_book.set_forbidden_debuffs(write_a_book_forbidden_debuffs)

# display the results:
oo_show_character_ability_to_perform_task(bob, climb_mountain)
oo_show_character_ability_to_perform_task(bob, cook_a_meal)
oo_show_character_ability_to_perform_task(bob, write_a_book)