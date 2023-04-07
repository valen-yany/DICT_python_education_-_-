import random
import sys


class RPS:
    def __init__(self):
        self.__option_list = ['rock', 'paper', 'scissors']
        self.__name = input('Enter your name:>')
        self.__points = 0
        with open('rating.txt', 'r') as f:
            for line in f:
                leader = line.split(' ')
                if self.__name == leader[0]:
                    self.__points = int(leader[1])
        while True:
            self.__game()

    def __computer_choice(self):
        return random.choice(self.__option_list)

    def __player_input(self):
        player_input = ''
        while player_input not in self.__option_list:
            player_input = input('>')
            if player_input == '!rating':
                print(f'Your rating: {self.__points}')
                continue
            elif player_input == '!exit':
                print('Bye!')
                sys.exit()
            elif player_input in self.__option_list:
                break
            print('Incorrect input:', end='')
        return player_input

    def __result(self, player, computer):
        if player == computer:
            print(f'There is a draw({computer})')
            self.__points += 50
        elif player == self.__option_list[self.__option_list.index(computer) - 1]:
            print(f'Sorry, but the computer chose {computer}')
        else:
            print(f'Well done. The computer chose {computer} and failed')
            self.__points += 100

    def __game(self):
        player_choice = self.__player_input()
        computer_choice = self.__computer_choice()
        self.__result(player_choice, computer_choice)


play = RPS()
