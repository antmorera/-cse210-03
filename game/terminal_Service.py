#I don't know if I need to have the import random in here for the read_number ?? So far this is what
#I have created in my not normal setup so this kinda like a wireframe that will use the inputs of the
#to be displayed on the screen and that can also be called by the director. 


###This code is still subject to changes or complete termination if is necessary###


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
