def is_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]               
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False


def is_draw(board):
    return " " not in board


def get_available_moves(board):
    return [i for i, space in enumerate(board) if space == " "]


def make_move(board, move, player):
    board[move] = player


def undo_move(board, move):
    board[move] = " "


def evaluate_board(board):
    if is_winner(board, "O"):
        return 10
    elif is_winner(board, "X"):
        return -10
    else:
        return 0


def minimax(board, depth, is_maximizing_player, alpha, beta):
    score = evaluate_board(board)

    if score == 10 or score == -10:
        return score

    if is_draw(board):
        return 0

    if is_maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            make_move(board, move, "O")
            eval = minimax(board, depth + 1, False, alpha, beta)
            undo_move(board, move)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            make_move(board, move, "X")
            eval = minimax(board, depth + 1, True, alpha, beta)
            undo_move(board, move)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval


def get_ai_move(board):
    best_move = -1
    best_score = float('-inf')

    for move in get_available_moves(board):
        make_move(board, move, "O")
        score = minimax(board, 0, False, float('-inf'), float('inf'))
        undo_move(board, move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def print_board(board):
    print("-------------")
    for i in range(0, 9, 3):
        print("|", board[i], "|", board[i+1], "|", board[i+2], "|")
        print("-------------")


def main():
    board = [" "] * 9
    current_player = "X"
    ai_player = "O"
    ai_turn = False

    while True:
        print_board(board)

        if current_player == "X":
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move < 0 or move >= 9 or board[move] != " ":
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Enter a number between 0 and 8.")
                continue
        else:
            move = get_ai_move(board)
            print(f"AI plays move {move+1}")

        make_move(board, move, current_player)

        if is_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()