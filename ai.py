from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
        # from parent class
        # self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        # self.chosen_gesture = ""
        # self.wins = 0

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f'ai has chosen {self.chosen_gesture}')