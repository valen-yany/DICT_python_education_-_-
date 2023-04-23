import random


def domino_create():
    domino_stack = []
    for i in range(0, 7):
        for j in range(i, 7):
            domino_stack.append((i, j))
    return domino_stack


def new_hand(stack):
    hand = []
    for i in range(0, 7):
        hand.append(random.choice(stack))
        stack.remove(hand[-1])
    return hand


def status_check(first_hand, second_hand):
    first_doubles = sorted([i for i in first_hand if i[0] == i[1]], key=lambda x: x[0], reverse=True)
    second_doubles = sorted([i for i in second_hand if i[0] == i[1]], key=lambda x: sum(x), reverse=True)
    if len(first_doubles) != 0 and len(second_doubles) != 0:
        if sum(first_doubles[0]) > sum(second_doubles[0]):
            return 1, first_doubles[0]
        if sum(second_doubles[0]) > sum(first_doubles[0]):
            return 2, second_doubles[0]
    if len(first_doubles) == 0:
        return 2, second_doubles[0]
    if len(second_doubles) == 0:
        return 1, first_doubles[0]
    return 0, None


def game():
    stack = domino_create()
    player_hand = []
    computer_hand = []
    reserve = []
    status = 0
    turn = ''
    first_turn = []
    snake = []
    while status == 0:
        reserve = stack[:]
        player_hand = new_hand(reserve)
        computer_hand = new_hand(reserve)
        status, first_turn = status_check(player_hand, computer_hand)
    if status == 1:
        turn = 'computer'
        player_hand.remove(first_turn)
    else:
        turn = 'player'
        computer_hand.remove(first_turn)
    snake += first_turn
    print(f'''Stock pieces: {reserve}
Computer pieces: {computer_hand}
Player pieces: {player_hand}
Snake: {snake}
Status: {turn}''')


game()
