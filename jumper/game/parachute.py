class Parachute:
    """Keeps track of the jumpers attempts and draws the picture
    
    Args: Create an instance of the jumper"""
    
    def __init__(self):
        
        self._picture = [' ___',
                         '/___\\',
                         '\   /',
                         ' \ /',
                         '  o',
                         ' /|\\',
                         ' / \\']
        self._attempts = 0
    
    def pop_list(self, answer):
    
        if answer == False:
            if self._attempts == 1:
                self._picture.pop(0)
            elif self._attempts == 2:
                self._picture.pop(0)
            elif self._attempts == 3:
                self._picture.pop(0)
            elif self._attempts == 4:
                self._picture.pop(0)
                self._picture[0] = "  x"
                
    def print_parachute(self):
        """Draws the picture by calling the list"""
        for lines in self._picture:
            print(lines)


