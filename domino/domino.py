import random


class Domino:
    def __init__(self):
        self.stack = []
        self.snake = []
        self.player = ('Player', 'PC')
        self.message = ('It\'s your turn to make a move. Enter your command:\n',
                        'Computer is about to make a move. Press Enter to continue...\n')
        self.turn = -1
        while self.turn == -1:
            self.domino_create()
            self.player_hand = self.new_hand()
            self.comp_hand = self.new_hand()
            self.status_check()
        self.game()

    def domino_create(self):
        for i in range(0, 7):
            for j in range(i, 7):
                self.stack.append([i, j])

    def new_hand(self):
        hand = []
        for i in range(0, 7):
            hand.append(random.choice(self.stack))
            self.stack.remove(hand[-1])
        return hand

    def status_check(self):
        first_doubles = sorted([i for i in self.player_hand if i[0] == i[1]], key=lambda x: x[0], reverse=True)
        second_doubles = sorted([i for i in self.comp_hand if i[0] == i[1]], key=lambda x: sum(x), reverse=True)
        if len(first_doubles) != 0 and len(second_doubles) != 0:
            if sum(first_doubles[0]) > sum(second_doubles[0]):
                self.turn = 1
                self.snake.append(first_doubles[0])
                self.player_hand.remove(first_doubles[0])
            elif sum(second_doubles[0]) > sum(first_doubles[0]):
                self.turn = 0
                self.snake.append(second_doubles[0])
                self.comp_hand.remove(second_doubles[0])
        elif len(first_doubles) == 0 and len(second_doubles) != 0:
            self.turn = 0
            self.snake.append(second_doubles[0])
            self.comp_hand.remove(second_doubles[0])
        elif len(second_doubles) == 0 and len(first_doubles) != 0:
            self.turn = 1
            self.snake.append(first_doubles[0])
            self.player_hand.remove(first_doubles[0])

    def player_turn(self):
        while True:
            turn = int(input())
            if turn > len(self.player_hand) or turn < -len(self.player_hand):
                print('Illegal move')
            elif turn == 0:
                if len(self.stack) > 0:
                    self.player_hand.append(random.choice(self.stack))
                    self.stack.remove(self.player_hand[-1])
                break
            elif turn > 0:
                if self.snake[-1][1] == self.player_hand[turn-1][0]:
                    self.snake += [self.player_hand[turn-1]]
                    self.player_hand.remove(self.player_hand[turn-1])
                    break
                elif self.snake[-1][1] == self.player_hand[turn-1][1]:
                    self.snake += [self.player_hand[turn - 1][::-1]]
                    self.player_hand.remove(self.player_hand[turn - 1])
                    break
                else:
                    print('Illegal move')
            elif turn < 0:
                if self.snake[0][0] == self.player_hand[-turn-1][1]:
                    self.snake = [self.player_hand[-turn-1]] + self.snake
                    self.player_hand.remove(self.player_hand[-turn - 1])
                    break
                elif self.snake[0][0] == self.player_hand[-turn-1][0]:
                    self.snake = [self.player_hand[-turn - 1][::-1]] + self.snake
                    self.player_hand.remove(self.player_hand[-turn - 1])
                    break
                else:
                    print('Illegal move')

    def check_draw(self):
        snake = ''
        for i in self.snake:
            snake += ''.join(list(map(str, i)))
        if snake.count(snake[0]) == 8 and snake.count(snake[-1]) == 8:
            return True
        return False

    def comp_turn(self):
        snake = ''
        for i in self.snake:
            snake += ''.join(list(map(str, i)))
        turns = [[snake.count(str(i[0])) + snake.count(str(i[1])), i] for i in self.comp_hand]
        turns.sort(key=lambda i: i[0], reverse=True)
        for turn in turns:
            if self.snake[-1][1] == turn[1][0]:
                self.snake += [turn[1]]
                self.comp_hand.remove(turn[1])
                return None
            elif self.snake[-1][1] == turn[1][1]:
                self.snake += [turn[1][::-1]]
                self.comp_hand.remove(turn[1])
                return None
            elif self.snake[0][0] == turn[1][1]:
                self.snake = [turn[1]] + self.snake
                self.comp_hand.remove(turn[1])
                return None
            elif self.snake[0][0] == turn[1][0]:
                self.snake = [turn[1][::-1]] + self.snake
                self.comp_hand.remove(turn[1])
                return None
        if len(self.stack) > 0:
            self.comp_hand.append(random.choice(self.stack))
            self.stack.remove(self.comp_hand[-1])

    def game(self):
        status = self.message[self.turn]
        while True:
            player_hand_formatted = [f'{num+1}: {piece}' for num, piece in enumerate(self.player_hand)]
            print(f'''{'=' * 70}
Stock size: {len(self.stack)}
Computer pieces: {len(self.comp_hand)}

Snake: {self.snake if len(self.snake) < 7 else f'{self.snake[:3]}...{self.snake[-3:]}'}

Your pieces: ''')
            for i in player_hand_formatted:
                print(i)
            print(f"\nStatus: {status}")
            if status not in self.message:
                break
            if self.player[self.turn] == 'Player':
                self.player_turn()
                if len(self.player_hand) == 0:
                    status = 'The game is over. You won!'
                    continue
            elif self.player[self.turn] == 'PC':
                input()
                self.comp_turn()
                if len(self.comp_hand) == 0:
                    status = 'The game is over. The computer won!'
                    continue
            if self.check_draw():
                status = 'The game is over. It\'s a draw!'
                continue
            self.turn = abs(self.turn - 1)
            status = self.message[self.turn]


D = Domino()


