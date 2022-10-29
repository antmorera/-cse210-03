from PuzzleWord import Puzzle_Word

class WordSlicer:  

    def _init(self):
        self._word = Puzzle_Word().randomWord()

    def slicer(self):
        self.sliced_word = list(self._word)
        return self.sliced_word