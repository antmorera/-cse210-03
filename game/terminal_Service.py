import random


class Console:
    "This class will is to get the text and numerical input from the user so it can display it. prompt (string): The prompt to display on each line."

    def read(self, prompt):
        "Gets text input from the user through the screen. Args Gets the text input from the user: self (Screen): An instance of Screen. prompt (string): The prompt to display to the user"
        
        return input(prompt)
    
    def read_number(self, prompt):
        "Gets numerical input from the user through the screen. Args: self (Screen): An instance of Screen. prompt (string): The prompt to display to the user. Returns:float: The user's input as a float."
        
        return float(input(prompt))

    def write(self, text):
        "Displays the given text on the screen. Args: self (Screen): An instance of Screen. text (string): The text to display."
        
        print(text)
