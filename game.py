from time import sleep
from human import Human
from ai import Ai
from player import Player
class Game:
    def __init__(self):
       self.player_one = None
       self.player_two = None
     

    def run_game(self):
        self.intro()
        self.number_of_players()
        self.play_rounds()
        self.display_winner()
        

    def intro(self):
        sleep(1)
        # print('\n\n\nWelcome to Rock Paper Scissors Lizard Spock.')
        # sleep(1)
        # print('\nEach match will be best of three games \nUse the number keys to enter your selection\n')
        # sleep(1)
        # print('Rock crushes Scissors')
        # sleep(1)
        # print('Scissors cuts Paper')
        # sleep(1)
        # print('Paper covers Rock')
        # sleep(1)
        # print('Rock crushes Lizard')
        # sleep(1)
        # print('Lizard poisons Spock')
        # sleep(1)
        # print('Spock smashes Scissors')
        # sleep(1)
        # print('Scissors decapitates Lizard')
        # sleep(1)
        # print('Lizard eats Paper')
        # sleep(1)
        # print('Paper disproves Spock')
        # sleep(1)
        # print('Spock vaporizes Rock')


    def number_of_players(self):
        user_choice = input('\nHow many players? 1, 2, or 3 for a surprise: ') 
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
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()

        
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                sleep(1)
                print("\nIt's a tie!")
            elif self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Scissors':
                sleep(1)
                print('\nPlayer 1 wins!')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Lizard':
                sleep(1)
                print('\nPlayer 1 wins!')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Paper':
                sleep(1)
                print('\nPlayer 1 wins!')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Lizard':
                sleep(1)
                print('\nPlayer 1 wins!')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Rock':
                sleep(1)
                print('\nPlayer 1 wins!')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Spock':
                sleep(1)
                print('\nPlayer 1 wins!')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Spock':
                sleep(1)
                print('\nPlayer 1 wins!')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Paper':
                sleep(1)
                print('\nPlayer 1 wins!')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Scissors':
                sleep(1)
                print('\nPlayer 1 wins!')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Rock':
                sleep(1)
                print('\nPlayer 1 wins!')
                self.player_one.wins += 1
            else:
                sleep(1)
                print("\nPlayer 2 wins!")
                self.player_two.wins += 1
    
    def display_winner(self):
        if self.player_one.wins == 2:
            sleep(1)
            print('\nPlayer One is the Grand Champion!\n')
        else:
            sleep(1)
            print('\nPlayer Two is the Grand Champion!\n')