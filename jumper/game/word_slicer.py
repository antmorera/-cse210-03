from game.puzzleword import PuzzleWord

class WordSlicer:  

    def __init__(self):
        self._word = PuzzleWord()._randomWord()

    def slicer(self):
        self.sliced_word = list(self._word)
        return self.sliced_word