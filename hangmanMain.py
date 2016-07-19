from hangmanClasses import Game

# Starting new hangman game
newGame = Game()

newGame.print_menu()
newGame.print_board()

for x in range(0, 6):
    newGame.numberMissed += 1
    newGame.print_board()
