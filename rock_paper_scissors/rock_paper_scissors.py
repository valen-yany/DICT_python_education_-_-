class RPS:
    def __init__(self):
        self.option_list = ['rock', 'paper', 'scissors']
        self.__game()

    def __player_turn(self):
        player_choice = input('>')
        while player_choice not in self.option_list:
            player_choice = input('Choice the correct option:\n>')
        return player_choice

    def __game(self):
        player_choice = self.__player_turn()
        print(f'Sorry, but the computer chose {self.option_list[self.option_list.index(player_choice) - 2]}')


play = RPS()
