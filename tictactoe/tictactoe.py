def tictactoe():
    game = [list("___"), list("___"), list("___")]
    player = "X"
    play_symbols = ["X", "O"]
    print("---------")
    print(f"|{'  '.join(game[0])}|\n|{'  '.join(game[1])}|\n|{'  '.join(game[2])}|")
    print("---------")
    while True:
        print("Enter the coordinates:", end='')
        coordinates = input().split(" ", 2)
        if not (coordinates[0].isnumeric() and coordinates[1].isnumeric()):
            print("You should enter numbers!")
            continue
        x_coordinate = int(coordinates[0]) - 1
        y_coordinate = int(coordinates[1]) - 1
        if not (-1 < x_coordinate < 3 and -1 < y_coordinate < 3):
            print("Coordinates should be from 1 to 3!")
            continue
        if game[x_coordinate][y_coordinate] != '_':
            print("This cell is occupied! Choose another one!")
            continue
        game[x_coordinate][y_coordinate] = player
        print("---------")
        print(f"|{'  '.join(game[0])}|\n|{'  '.join(game[1])}|\n|{'  '.join(game[2])}|")
        print("---------")
        if (game[0].count(player * 3) + game[1].count(player * 3) + game[2].count(player * 3) + (
                game[0][0] + game[1][1] + \
                game[2][2]).count(player * 3) + (game[0][2] + game[1][1] + game[2][0]).count(player * 3) + (
                    game[0][0] + game[1][0] + \
                    game[2][0]).count(player * 3) + (game[0][1] + game[1][1] + game[2][1]).count(player * 3) + (
                    game[0][2] + game[1][2] + \
                    game[2][2]).count(player * 3)) == 1:
            print(f"{player} wins")
            return None
        if '_' not in game[0] and '_' not in game[1] and '_' not in game[2]:
            print("Draw")
            return None
        player = play_symbols[abs(play_symbols.index(player) - 1)]


tictactoe()
