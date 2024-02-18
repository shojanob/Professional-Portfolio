# For Loop List Iteration
nums = [1, 2, 3]
new_nums = []
for n in nums:
    add_1 = n + 1
    new_nums.append(add_1)

# List Comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

# String as List Comprehension
name = "Angela"
new_list = [letter for letter in name]

# Range as List Comprehension
double_list = [num * 2 for num in range (1,5)]

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor"]
short_names = [name for name in names if len(name) < 5]

all_caps = [name.upper() for name in names if len(name) > 5]