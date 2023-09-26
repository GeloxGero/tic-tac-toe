def print_board(board):
    for row in board:
        print(' '.join(row))

def check_win(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '[ ]':
            return True
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != '[ ]':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '[ ]':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '[ ]':
        return True        
    return False        

def tic_tac_toe():
    board = [['[ ]' for _ in range(3)] for _ in range(3)]
    current_player = '[x]'
    
    while True:
        print_board(board)
        print("Current Player: ", current_player)
        
        while True:
            try:
                row = int(input("Enter the row number (1-3): ")) - 1
                col = int(input("Enter the column number (1-3): ")) - 1
                
                if row in range(3) and col in range(3) and board[row][col] == '[ ]':
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")
        
        board[row][col] = current_player
        if check_win(board):
            print(f"Player {current_player} wins!")
            break
        
        current_player = '[o]' if current_player == '[x]' else '[x]'

tic_tac_toe()