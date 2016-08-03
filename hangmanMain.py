# hangmanMain.py
# Author: Brindan Jackson
# Description: The game of hangman played through the console.

from hangmanClasses import Game
from random import randint

# Starting new hangman game
newGame = Game()

while not newGame.is_game_finished():
    newGame.print_menu()

    menuChoice = input("Select a menu option: ")

    if menuChoice not in ['1', '2', '3']:
        print("Not a valid input. Please try again.")

    elif menuChoice == '1':
        wordsFile = open("hangman_words.txt")
        fileContents = wordsFile.read()
        wordsFile.close()

        wordArray = fileContents.split("\n")

        newGame.gameWord = wordArray[randint(0, len(wordArray)-1)]
        newGame.gameHiddenWord = "_ " * len(newGame.gameWord)

        while not(newGame.is_round_finished()):
            newGame.print_board()
            newGame.print_hidden_word()

            choiceOk = 1

            while choiceOk > 0:
                letterChoice = input("Pick a letter: ")

                if letterChoice > 0:
                    print("Letter already chosen: ")

    elif menuChoice == '2':
        print("Help Menu")

    elif menuChoice == '3':
        print("Game Ended")
        newGame.set_game_finished(1)
