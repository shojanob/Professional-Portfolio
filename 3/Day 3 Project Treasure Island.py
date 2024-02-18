# Make your own "Choose Your Own Adventure" game.
# Use conditionals such as `if`, `else`, and `elif` statements to lay out the logic and the story's path in your program.


print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_step = input('You\'re stranded on the beach, where do you want to go? Type "left" or "right"\n').lower()
if first_step == "left":
    second_step = input('You come to a jungle. There is a huge hut in the middle of the jungle. Type "go" to go to the hut. '
          'Type "ignore" to ignore the hut and go around.\n').lower()
    if second_step == "go":
        print("You were attacked by a tribe inside the hut. Game Over.")
    elif second_step == "ignore":
        final_step = input("You successfully managed to get passed the dangerous tribe. There are three waterfalls with different colors. "
              "One blue, one black and one green. Which color waterfall do you choose to go through?\n ").lower()
        if final_step == "blue":
            print("You fell into a giant hole. Game Over.")
        elif final_step == "green":
            print("You got eaten by vultures. Game Over.")
        elif final_step == "black":
            print("You WIN!, You successfully found the treasure!")
        else:
            print("Game Over. Follow the rules and answer with the given options.")
    else:
        print("Game Over. Follow the rules and answer with the given options.")
elif first_step == "right":
    print("You were attacked by a group of crabs. Game Over.")
else:
    print("Game Over. Follow the rules and answer with the given options.")