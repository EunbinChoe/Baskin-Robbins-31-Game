import game_structure

# main for basic structure of the Baskin-Robbins 31 game
# that can be played through the terminal

# instruction
print("Baskin-Robbins 31 game")
print('''
To learn how to play, type help
To start the game, type start
To quit game, type quit''')

while True:
    menu = input("> ").lower()

    if menu == "help":
        print("How to play: \nFirst, choose whether to start first or not.\n"
              "Next, you and the computer each say 1-3 consecutive numbers at their turn starting with 1.\n"
              "On your turn, to type how many numbers you want to say. From 1-3\n" 
              "If the computer says 31, you win.\n"
              "If you say 31, you lose.\n"
              "Enjoy the game!!")

    elif menu == "start":
        level = int(input("Choose level \n\"1\" for basic mode \n\"2\" for normal mode \n\"3\" for difficult mode\n"
                          "~ "))
        first_to_go = bool(int(input("Would you like to go first? (\"1\" to go first, \"0\" to go second) \n~ ")))
        while level < 1 or level > 3:
            level = int(input("Wrong input for level. \nRe-enter \n~ "))
        if level == 1:
            start = game_structure.BasicMode(first_to_go)
            start.start_game()
        elif level == 2:
            start = game_structure.NormalMode(first_to_go)
            start.start_game()
        else:
            start = game_structure.DiffNode(first_to_go)
            start.start_game()

        first_to_go = False

    elif menu == "quit":
        break

    else:
        print("Sorry didn't understand that. Try again")

