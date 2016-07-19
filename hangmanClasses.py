class Game:
    def __init__(self):
        # Setting up game menu displayed at start
        self.gameMenu = "********************\n"
        self.gameMenu += "|Welcome to Hangman|\n"
        self.gameMenu += "|                  |\n"
        self.gameMenu += "| 1.) Play Hangman |\n"
        self.gameMenu += "| 2.) Help         |\n"
        self.gameMenu += "| 3.) Quit         |\n"
        self.gameMenu += "|                  |\n"
        self.gameMenu += "********************\n"

        # Setting up initial game board
        # Top of Game Board
        self.gameBoardTop = "    ______\n"
        self.gameBoardTop += "   |      |\n"

        self.gameBoardHead = ["   |\n", "   |      O\n"]
        self.gameBoardArms = ["   |\n", "   |      |\n", "   |     /|\n", "   |     /|\\\n"]
        self.gameBoardLegs = ["   |\n", "   |     /\n", "   |     / \\\n"]

        self.gameBoardBottom = "___|______\n"

        self.gameWord = ""
        self.gameHiddenWord = ""
        self.roundFinished = 0
        self.numberMissed = 0
        self.gameFinished = 0

    def print_menu(self):
        print(self.gameMenu)

    def print_board(self):
        if self.numberMissed == 0:
            print(self.gameBoardTop +
                  self.gameBoardHead[0] +
                  self.gameBoardArms[0] +
                  self.gameBoardLegs[0] +
                  self.gameBoardBottom)

        elif self.numberMissed == 1:
            print(self.gameBoardTop +
                  self.gameBoardHead[1] +
                  self.gameBoardArms[0] +
                  self.gameBoardLegs[0] +
                  self.gameBoardBottom)

        elif self.numberMissed == 2:
            print(self.gameBoardTop +
                  self.gameBoardHead[1] +
                  self.gameBoardArms[1] +
                  self.gameBoardLegs[0] +
                  self.gameBoardBottom)

        elif self.numberMissed == 3:
            print(self.gameBoardTop +
                  self.gameBoardHead[1] +
                  self.gameBoardArms[2] +
                  self.gameBoardLegs[0] +
                  self.gameBoardBottom)

        elif self.numberMissed == 4:
            print(self.gameBoardTop +
                  self.gameBoardHead[1] +
                  self.gameBoardArms[3] +
                  self.gameBoardLegs[0] +
                  self.gameBoardBottom)

        elif self.numberMissed == 5:
            print(self.gameBoardTop +
                  self.gameBoardHead[1] +
                  self.gameBoardArms[3] +
                  self.gameBoardLegs[1] +
                  self.gameBoardBottom)

        elif self.numberMissed == 6:
            print(self.gameBoardTop +
                  self.gameBoardHead[1] +
                  self.gameBoardArms[3] +
                  self.gameBoardLegs[2] +
                  self.gameBoardBottom)

    def print_word(self):
        print(self.gameWord)

    def print_hidden_word(self):
        print(self.gameHiddenWord)

    def set_round_finished(self, finished):
        self.roundFinished = finished

    def set_missed(self, number_missed):
        self.numberMissed = number_missed

    def set_game_finished(self, finished):
        self.gameFinished = finished

    def is_game_finished(self):
        if self.gameFinished == 1:
            return True
        else:
            return False
