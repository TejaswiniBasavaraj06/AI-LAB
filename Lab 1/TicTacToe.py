import random

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
    return False

def check_draw(board):
    return all(space in ['X', 'O'] for space in board)

def main():
    print(" TIC-TAC-TOE GAME (HUMAN vs CPU) ")
    board = [str(i + 1) for i in range(9)] 
    human = 'X'
    computer = 'O'
    current_turn = human
    print_board(board)
    while True:
        if current_turn == human:
            print("Human's Turn (X)")
            try:
                move = int(input("Enter position (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] in ['X', 'O']:
                    print("Invalid move or spot taken. Choose an open spot (1-9).")
                    continue
                board[move] = human
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
        else:
            print("Computer's Turn (O)")
            available_moves = [i for i in range(9) if board[i] not in ['X', 'O']]
            move = random.choice(available_moves)
            board[move] = computer
            print(f"Computer played 'O' at position {move + 1}")
        print_board(board)

        if check_win(board, current_turn):
            if current_turn == human:
                print("You Won!")
            else:
                print("Computer Won!")
            break

        if check_draw(board):
            print("Draw!!")
            break

        current_turn = computer if current_turn == human else human

if __name__ == "__main__":
    main()