import random

class RPS:
    def __init__(self):
        self.__option_list = ['rock', 'paper', 'scissors']
        self.__game()

    def __computer_choice(self):
        return random.choice(self.__option_list)

    def __player_turn(self):
        player_choice = input('>')
        while player_choice not in self.__option_list:
            player_choice = input('Choice the correct option:\n>')
        return player_choice

    def __result(self, player, computer):
        if player == computer:
            print(f'There is a draw({computer})')
        elif player == self.__option_list[self.__option_list.index(computer) - 1]:
            print(f'Sorry, but the computer chose {computer}')
        else:
            print(f'Well done. The computer chose {computer} and failed')

    def __game(self):
        player_choice = self.__player_turn()
        computer_choice = self.__computer_choice()
        self.__result(player_choice, computer_choice)


play = RPS()
