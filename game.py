from time import sleep
from human import Human
from ai import Ai
class Game:
    def __init__(self):
       self.player_one = None
       self.player_two = None

    def run_game(self):
        self.intro()
        self.number_of_players()
        

    def intro(self):
        sleep(1)
        print('\n\n\nWelcome to Rock Paper Scissors Lizard Spock.')
        sleep(1)
        print('\nEach match will be best of three games \nUse the number keys to enter your selection\n')
        sleep(1)
        print('Rock crushes Scissors')
        sleep(1)
        print('Scissors cuts Paper')
        sleep(1)
        print('Paper covers Rock')
        sleep(1)
        print('Rock crushes Lizard')
        sleep(1)
        print('Lizard poisons Spock')
        sleep(1)
        print('Spock smashes Scissors')
        sleep(1)
        print('Scissors decapitates Lizard')
        sleep(1)
        print('Lizard eats Paper')
        sleep(1)
        print('Paper disproves Spock')
        sleep(1)
        print('SPock vaporizes Rock')


    def number_of_players(self):
        user_choice = input('How many players? 1, 2, or 3 for a surprise ') 
        if user_choice == "1":
            self.player_one = Human()
            self.player_two = Ai()
        elif user_choice == "2":
            self.player_one = Human()
            self.player_two = Human()
        elif user_choice == "3":
            self.player_one = Ai()
            self.player_two = Ai()

    def play_rounds(self):
        pass
