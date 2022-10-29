from game.parachutetracker import ParachuteTracker
from game.wordslicer import WordSlicer
from game.gametitle import GameTitle


class Director:
    """This class will follow the flow of the game
    """

    def __init__(self) -> None:
        self._sliced_word = WordSlicer()
        self._parachuteTracker = ParachuteTracker()
        self._game_title = GameTitle()
        self._guessed = False
        self._user_guess = ""
        self._user_guesses = []
        self._tries = 5
        self._guess_word = self._sliced_word.slicer()

    def startGame(self):
        """Starts the game by running the main game loop"""
        pass

    def _display(self):
        """Display in the console the flow of the
        game for inputs and outputs.
        """
        pass

    # Logic of the game
    def _wordTracker(self):
        """This Method will evaluate the word and the letter
        that the user what to guess from the jumper
        Also it update the jumper graph
        """
        while not self._guessed:
            self._display()
            # print(f"\nUncovered word: {''.join(self._guess_word)}\n\n")
            self._parachuteTracker.parachuteChooser(self._tries)
            # Word exchange logic
            for letter in self._guess_word:
                if letter in self._user_guesses:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")

            self._user_guess = input("\n\n\nPlease guess a letter: ").upper()
            self._user_guesses.append(self._user_guess.upper())

            if self._user_guess.upper() not in self._guess_word:
                self._tries -= 1
                if self._tries == 0:
                    break

            self._guessed = True
                        
            for letter in self._guess_word:
                if letter not in self._user_guesses:
                    self._guessed = False
        
        if self._guessed:
            self._gameWin()
        else:
            self._gameOver()


    def _gameOver(self):
        pass
    def _gameWin(self):
        pass