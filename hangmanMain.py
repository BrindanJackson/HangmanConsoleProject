from hangmanClasses import Game

# Starting new hangman game
newGame = Game()

while newGame.roundFinished == 0:
    newGame.print_menu()

    menuChoice = input("Select a menu option: ")

    if menuChoice not in ['1', '2', '3']:
        print("Not a valid input. Please try again.")

    elif menuChoice == '1':
        print("Play game")

    elif menuChoice == '2':
        print("Help Menu")

    elif menuChoice == '3':
        print("Game Ended")
        newGame.set_round_finished(1)
