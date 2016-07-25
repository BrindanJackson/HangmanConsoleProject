# hangmanMain.py
# Author: Brindan Jackson
# Description: The game of hangman played through the console.

from hangmanClasses import Game

# Starting new hangman game
newGame = Game()

while newGame.gameFinished == 0:
    newGame.print_menu()

    menuChoice = input("Select a menu option: ")

    if menuChoice not in ['1', '2', '3']:
        print("Not a valid input. Please try again.")

    elif menuChoice == '1':
        wordsFile = open("hangman_words.txt")

        wordsFile.close()

        while newGame.roundFinished == 0:
            pass

    elif menuChoice == '2':
        print("Help Menu")

    elif menuChoice == '3':
        print("Game Ended")
        newGame.set_game_finished(1)
