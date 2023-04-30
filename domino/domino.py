import random


def game():
    stack = domino_create()
    player_hand = []
    computer_hand = []
    reserve = []
    status = 0
    turn = ''
    message = ''
    first_turn = []
    snake = []
    while status == 0:
        reserve = stack[:]
        player_hand = new_hand(reserve)
        computer_hand = new_hand(reserve)
        status, first_turn = status_check(player_hand, computer_hand)
    if status == 1:
        turn = 'player'
        message = 'It\'s your turn to make a move. Enter your command.'
        player_hand.remove(first_turn)
    else:
        turn = 'computer'
        message = 'Computer is about to make a move. Press Enter to continue...'
        computer_hand.remove(first_turn)
    snake += first_turn
    player_hand_formatted = [f'{num}: {piece}' for num, piece in enumerate(player_hand)]
    print(f'''{'=' * 70}
Stock size: {len(reserve)}
Computer pieces: {len(computer_hand)}

Snake: {snake}

Your pieces: ''')
    for i in player_hand_formatted:
        print(i)
    print(f"\nStatus: {message}")

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

game()
