# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# (3.2)
# It should tell them the interpretation of their BMI based on the BMI value.

# - Under 18.5 they are underweight
# - Over 18.5 but below 25 they have a normal weight
# - Over 25 but below 30 they are slightly overweight
# - Over 30 but below 35 they are obese
# - Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(weight) / float(height) ** 2

bmi_index = f"Your BMI is {int(BMI)}, "

if BMI < 18.5:
    print(bmi_index + " you are underweight")
elif BMI > 18.5 and BMI < 25:
    print(bmi_index + " you have a normal weight.")
elif BMI > 25 and BMI < 30:
    print(bmi_index + " you are slightly overweight.")
elif BMI > 30 and BMI < 35:
    print(bmi_index + " you are obese.")
else:
    print(bmi_index + " you are clinically obese")