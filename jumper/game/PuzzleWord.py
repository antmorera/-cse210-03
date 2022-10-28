import random

class Puzzle_Word:

    def __init__(self):

        self._wordlist = []


    def randomWord(self):

        self.load_list()
        my_random_word = random.choice(self.wordlist)
        return my_random_word.upper()

    def load_list(self):

        with open("wordlist.txt", "rt") as text_file:
            read_data = text_file.readlines()
            for line in read_data:
                clean_line = line.strip()
                self._wordlist.append(clean_line)

def main():
    pass

if (__name__ == "__main__"):
    main()