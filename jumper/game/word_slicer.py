from puzzleword import PuzzleWord

class WordSlicer:  

    def _init(self):
        self._word = PuzzleWord().randomWord()

    def slicer(self):
        self.sliced_word = list(self._word)
        return self.sliced_word