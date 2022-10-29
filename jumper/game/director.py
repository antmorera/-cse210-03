from game.parachute import Parachute
from game.puzzleword import PuzzleWord

class Director:

    def __init__(self):

        self.parachute = Parachute()
        self.keep_playing = True
        self.puzzleword = PuzzleWord()
        self.Letter_used = ""

    def start_game(self):

        while self.keep_playing:

            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def do_outputs(self):

        self.puzzleword.randomWord()
        self.parachute.print_parachute()

    def get_inputs(self):

        self.Letter_used= self.terminal_service.read("Guess a letter: ")

    def do_updates(self):

        correct_guess = self.puzzleword.process_guess(self.Letter_used)
        if correct_guess == False:
            self.parachute.pop_list()
        
        if self.keep_playing() == True:
        
            if self.parachute.keep_playing() == True:
                self.keep_playing == True

            else:

                self.keep_playing = False
                self.parachute.change_parachute()
                self.parachute.print_parachute()
        
        else:
            self.keep_playing = False
