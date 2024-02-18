# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35,
# then the output should be 3 + 5 = 8

# **Warning.** Do not change the code on lines 1-3. Your program should work for different inputs.
# e.g. any two-digit number.

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

new_two_digit_number = str(two_digit_number)

first_digit = (new_two_digit_number[0])
second_digit = (new_two_digit_number[1])
total_num = int(first_digit) + int(second_digit)
print(first_digit + " + " + second_digit + " = " + str(total_num))
print(total_num)