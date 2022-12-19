class Player:
    
    def __init__(self):
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.options_list = ['0', '1', '2', '3', '4'] # Need list to validate user input
        self.chosen_gesture = ""
        self.wins = 0
        # self.rock = self.gestures[0] = 0
        # self.paper = self.gestures[1] = 1
        # self.scissors = self.gestures[2] = 2
        # self.lizard = self.gestures[3] = 3
        # self.spock = self.gestures[4] = 4