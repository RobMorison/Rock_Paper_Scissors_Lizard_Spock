from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        # from parent class
        # self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        # self.chosen_gesture = ""
        # self.wins = 0

    def choose_gesture(self): # give user options with input ex 'press 0 to select rock, 1 for paper  
        # if we gather a number that aligns with their index position we can use that user input as the index position
        
        self.user_choice = input('\nChoose 0 for Rock\nChoose 1 for Paper\nChoose 2 for Scissors\nChoose 3 for Lizard\nChoose 4 for Spock\n\nChoose your gesture: ')
        self.chosen_gesture = self.gestures[int(self.user_choice)] # convert user input to int() and replace 0 with that user input variable
        print(f'You have chosen {self.chosen_gesture}')

        