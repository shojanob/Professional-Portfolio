# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
#
# The position and number of hurdles changes each time this world is reloaded.
# What you need to know
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.



# def turn_around():
#     turn_left()
#     turn_left()
#
#
# def go_up_down():
#     turn_left()
#     move()
#
#
# def turn_right():
#     turn_around()
#     turn_left()
#
#
# def bottom_to_top():
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     move()
#
#
# while at_goal() == False:
#     if wall_in_front() == True:
#         jump()
#         bottom_to_top()
#     elif front_is_clear() == True:
#         move()