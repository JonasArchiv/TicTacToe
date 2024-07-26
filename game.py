def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Spieler {current_player}, wähle eine Position (1-9): ")
        try:
            move = int(input()) - 1
            if move < 0 or move >= 9:
                print("Ungültige Position. Bitte wähle eine Zahl zwischen 1 und 9.")
                continue
            row, col = divmod(move, 3)
            if board[row][col] != " ":
                print("Diese Position ist bereits belegt. Wähle eine andere Position.")
                continue
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Spieler {winner} hat gewonnen!")
                break
            if is_full(board):
                print_board(board)
                print("Unentschieden!")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

tic_tac_toe()
