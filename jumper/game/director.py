from game.terminal_Service import Terminal_Service
from game.parachute import Parachute
from game.PuzzleWord import Puzzle_Word

class Director:

    def __init__(self):

        self.terminal_service = Terminal_Service()
        self.parachute = Parachute()
        self.keep_playing = True
        self.puzzleword = Puzzle_Word()
        self.Letter_used = ""

    def start_game(self):

        while self.keep_playing:

            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def do_outputs(self):

        self.puzzleword.draw_word()
        self.parachute.picture()

    def get_inputs(self):

        self.Letter_used= self.terminal_service.read("Guess a letter: ")

    def do_updates(self):

        correct_guess = self.puzzleword.process_guess(self.Letter_used)
        if correct_guess == False:
            self.parachute.remove_parachute_part()
        
        if self.puzzleword.keep_playing() == True:
        
            if self.parachute.keep_playing() == True:
                self.keep_playing == True

            else:

                self.keep_playing = False
                self.parachute.change_parachute()
                self.parachute.picture()
        
        else:
            self.keep_playing = False
