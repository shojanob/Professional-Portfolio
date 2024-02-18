# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# > Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.


# For Love Scores **less than 10** or **greater than 90**, the message should be:

# `"Your score is **x**, you go together like coke and mentos."`

# For Love Scores **between 40** and **50**, the message should be:

# `"Your score is **y**, you are alright together."`

# Otherwise, the message will just be their score. e.g.:

# `"Your score is **z**."`

# e.g.

# `name1 = "Angela Yu"`

# `name2 = "Jack Bauer"`

# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# My solution
name1_lower = name1.lower()
name2_lower = name2.lower()

t_count_name1 = name1_lower.count("t")
r_count_name1 = name1_lower.count("r")
u_count_name1 = name1_lower.count("u")
e_count_name1 = name1_lower.count("e")

t_count_name2 = name2_lower.count("t")
r_count_name2 = name2_lower.count("r")
u_count_name2 = name2_lower.count("u")
e_count_name2 = name2_lower.count("e")

total_true_count = (t_count_name1 + r_count_name1 + u_count_name1 + e_count_name1 +
                    t_count_name2 + r_count_name2 + u_count_name2 + e_count_name2)

l_count_name1 = name1_lower.count("l")
o_count_name1 = name1_lower.count("o")
v_count_name1 = name1_lower.count("v")

l_count_name2 = name2_lower.count("l")
o_count_name2 = name2_lower.count("o")
v_count_name2 = name2_lower.count("v")

total_love_count = (l_count_name1 + o_count_name1 + v_count_name1 + e_count_name1 +
                    l_count_name2 + o_count_name2 + v_count_name2 + e_count_name2)

str_total_count = str(total_true_count) + str(total_love_count)
love_score = int(str_total_count)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
if love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

# Other solution
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))

# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")

