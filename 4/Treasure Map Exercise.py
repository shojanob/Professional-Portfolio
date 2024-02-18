# You are going to write a program which will mark a spot with an X.

# In the starting code, you will find a variable called ```map```.

# This ```map``` contains a nested list.
# When ```map``` is printed this is what the nested list looks like:
# ```
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# ```
# In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:
# ```
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ```
# This is to try and simulate the coordinates on a real map.

# ![](https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1440,f_auto/Co-ordinates_oggjzg.jpg)

# Your job is to write a program that allows you to mark a square on the map using a two-digit system.
# The first digit for the input will specify the column (the position on the horizontal axis).
# The second digit in the input will specify the row number (the position on the vertical axis).

# First your program must take the user input and convert it to a usable format.

# Next, you need to use it to update your nested list with an "x".

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")