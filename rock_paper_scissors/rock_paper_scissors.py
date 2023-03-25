import random


class RPSGame:
    def __init__(self):
        self.name = input('Enter your name:>')
        self.points = 0
        with open('rating.txt') as f:
            for string in f:
                player = string.split()
                if self.name in player:
                    self.points = int(player[1])
                    break
        print(f'Hello, {self.name}')
        self.option_list = input('>').split(',')
        if len(self.option_list) < 3:
            self.option_list = ['rock', 'paper', 'scissors']
        self.game()

    def game(self):
        print('Okay, let`s start')
        while True:
            player_choice = self.player_input()
            if player_choice == '!exit':
                print('Bye!')
                break
            if player_choice == '!rating':
                print(f'Your rating: {self.points}')
                continue
            comp_choice = self.computer_choice()
            self.points += self.result(player_choice, comp_choice)

    def player_input(self):
        option = input('>')
        while option not in self.option_list and option != '!exit' and option != '!rating':
            option = input('Invalid input!\n>')
        return option

    def computer_choice(self):
        return random.choice(self.option_list)

    def result(self, player_choice, comp_choice):
        lose = self.option_list[self.option_list.index(player_choice) - round(len(self.option_list) / 2):
                               self.option_list.index(player_choice): -1]
        if comp_choice in lose:
            print(f'Sorry, but the computer chose {comp_choice}')
            return 0
        elif comp_choice == player_choice:
            print(f'There is a draw ({comp_choice})')
            return 50
        else:
            print(f'Well done. The computer chose {comp_choice} and failed')
            return 100


Game = RPSGame()


