from player import Player
from time import sleep

class Human(Player):
    def __init__(self):
        super().__init__()
        # from parent class
        # self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        # self.chosen_gesture = ""
        # self.wins = 0

    def choose_gesture(self): # give user options with input ex 'press 0 to select rock, 1 for paper  
        # if we gather a number that aligns with their index position we can use that user input as the index position
        
        
        
        self.valid_gesture = False

        while self.valid_gesture == False:
            self.user_choice = input('\nChoose 0 for Rock\nChoose 1 for Paper\nChoose 2 for Scissors\nChoose 3 for Lizard\nChoose 4 for Spock\n\nChoose your gesture: ')       
            self.chosen_gesture = int(self.user_choice) # convert user input to int() and replace 0 with that user input variable   
            if self.chosen_gesture == 0:
                print(f'You have chosen {self.gestures[0]}')
                self.valid_gesture = True
            elif self.chosen_gesture == 1:
                print(f'YOu have chosen {self.gestures[1]}')
                self.valid_gesture = True
            elif self.chosen_gesture == 2:
                print(f'You have chosen {self.gestures[2]}')
                self.valid_gesture = True
            elif self.chosen_gesture == 3:
                print(f'You have chosen {self.gestures[3]}')
                self.valid_gesture = True
            elif self.chosen_gesture == 4:
                print(f'You have chosen {self.gestures[4]}')
                self.valid_gesture = True
            else:
                print('Invalid selection. Choose again')