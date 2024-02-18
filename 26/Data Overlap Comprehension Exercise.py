# Take a look inside **file1.txt** and **file2.txt**. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
# e.g. if file1.txt contained:
#
# ```
# 1
# ```
#
# ```
# 2
# ```
#
# ```
# 3
# ```
#
# and file2.txt contained:
#
# ```
# 2
# ```
#
# ```
# 3
# ```
#
# ```
# 4
# ```
#
# ```
# result = [2, 3]
# ```
#
# **IMPORTANT**: The result should be a list that contains **Integers**, not **Strings**.
# Try to use **List Comprehension** instead of a **Loop**.
#
# Example Output
#
# ```
# [3, 6, 5, 33, 12, 7, 42, 13]

first_nums = []
second_nums = []

with open("file1.txt", mode= "r") as first_file:
    nums = first_file.readlines()
    for num in nums:
        first_nums.append(num)
with open("file2.txt", mode="r") as second_file:
    nums_2 = second_file.readlines()
    for n in nums_2:
        second_nums.append(n)

first_nums.extend(second_nums)

result = [numbers for numbers in first_nums if first_nums.count(numbers) > 1]

print(result)
