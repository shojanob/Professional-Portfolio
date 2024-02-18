# Assigning variables in Python (1.4)

name = "Jack"
print(name)

name = "Angela"
print(name)

name = input("What is your name?")
length = len(name)
print(length)

# Write a program that switches the values stored in the variables a and b. (1.4)
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)