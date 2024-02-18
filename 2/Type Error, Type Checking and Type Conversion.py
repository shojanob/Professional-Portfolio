# (2.2)
# Type Error
num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")

#Type Checking
print(type(num_char))

a = str(123)
print(type(a))

a = float(123)
print(type(a))

#Type Conversion
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

print(70 + float(100.5))
print(str(70) + str(100))
