from hangmanClasses import Game

# Starting new hangman game
newGame = Game()

newGame.printMenu()
newGame.printBoard()

for x in range(0,6):
    newGame.numberMissed += 1
    newGame.printBoard()
