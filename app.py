
board = [[' ']*3 for _ in range(3)]

def print_board():
    for row in board:
        print('|'.join(row))
        
def check_winner():
    # Check rows
    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 'X'
        elif all(board[row][col] == 'O' for row in range(3)):
            return 'O'
    
    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 'O'
    
    return None
def is_board_full():
    for row in board:
        if ' ' in row:
            return False  # If any cell is empty, the board is not full
    return True
   
def main():
 current_player = 'X'

 while True:
    print_board()
    
    row = int(input('Enter row (0, 1, 2): '))
    col = int(input('Enter column (0, 1, 2): '))
    
    if board[row][col] == ' ':
        board[row][col] = current_player
        winner = check_winner()
        
        if winner:
            print_board()
            print(f'Player {winner} wins!')
            break
        elif is_board_full():
                print_board()
                print("It's a draw!")
                break
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print('Cell already taken. Try again.')
if __name__ == "__main__":
    main()
  