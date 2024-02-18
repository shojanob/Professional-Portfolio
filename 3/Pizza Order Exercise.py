# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.


# Small Pizza: $15


# ```
# Medium Pizza: $20
# ```

# ```
# Large Pizza: $25
# ```

# ```
# Pepperoni for Small Pizza: +$2
# ```

# ```
# Pepperoni for Medium or Large Pizza: +$3
# ```

# ```
# Extra cheese for any size pizza: + $1

size = input("size = ")
add_pepperoni = input("add_pepperoni = ")
extra_cheese = input("extra_cheese = ")

bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
if size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
if size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1


print(f"Your final bill is ${bill}")



