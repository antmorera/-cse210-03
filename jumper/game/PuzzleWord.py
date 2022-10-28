import random

word_list = []

with open("wordlist.txt") as file:

    for line in file.readlines():
        for word in line.split("\n"):
            if len(word) == 5:
                word_list.append(word)

class Puzzle_Word:

    def __init__(self, word_list):

        word_random = random.SystemRandom()
        word_choice = word_random.choice(word_list)
        self.word_choice = word_choice

    def start_game(self):

        alternative = " "
        wrong_letter_try = 0
        counter_w = 0

        while alternative != "q":

            choice = self.word_choice
            print(choice)
            letters = []
            letters_used = []
            letters.clear()

            for letter in choice:
                letters.append(letter)

            wrong_guessing = 0
            give_up = 0
            letters_trial = 0
            wrong_letter_try = 0
            counter_w = counter_w +1

            print("Start guessing!")

            guessing = ["_", "_", "_", "_", "_", "_"]

            guess_letter = ""

            for w in guessing:
                guess_letter = guess_letter + w

                print("\n\nCurrent Guess: " + guess_letter)
                print ("\n  _____ \n /_____\ \n \     / \n  \   /  \n    0 \n   /|\ \n   / \ \n \n^^^^^^^\n")
                
                keep_playing = True

     #Needs to be added an interactive keep playing code for the user and some print messages when the game starts, ends.          


Puzzle_Word(word_list).game_begin()