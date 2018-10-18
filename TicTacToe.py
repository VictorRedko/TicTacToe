def print_board(board):
    """Prints the board."""

    board_copy = board.copy()
    for n in range(9): 
        if board_copy[n] is None: board_copy[n] = n+1
    print('\n {}\t{}\t{}\n'.format(board_copy[0], board_copy[1], board_copy[2]))
    print('\n {}\t{}\t{}\n'.format(board_copy[3], board_copy[4], board_copy[5]))
    print('\n {}\t{}\t{}'.format(board_copy[6], board_copy[7], board_copy[8]))


def game_won(board):
    """Determines whether the game is over yet.

    Checks every row, column, and diagonal to see if they are equal. If yes,
    and if they are nonempty, it returns the code corresponding to the winner,
    be it X or O. Otherwise, it returns the code for an unfinished game.

    Args:
        board: The board represented as a list.

    Returns:
        A code, between 0, 1, and 2, based on the end condition:
        
        0: The game is not yet over.
        1: X has won.
        2: O has won.
    """

    if board[0] == board[1] == board[2] is not None:
        if board[0] == 'X': 
            return 1
        else: 
            return 2
    elif board[3] == board[4] == board[5] is not None:
        if board[3] == 'X': 
            return 1
        else: 
            return 2
    elif board[6] == board[7] == board[8] is not None:
        if board[6] == 'X': 
            return 1
        else: 
            return 2
    elif board[0] == board[3] == board[6] is not None:
        if board[0] == 'X': 
            return 1
        else: 
            return 2
    elif board[1] == board[4] == board[7] is not None:
        if board[1] == 'X': 
            return 1
        else: 
            return 2
    elif board[2] == board[5] == board[8] is not None:
        if board[2] == 'X': 
            return 1
        else: 
            return 2
    elif board[0] == board[4] == board[8] is not None:
        if board[0] == 'X': 
            return 1
        else: 
            return 2
    elif board[2] == board[4] == board[6] is not None:
        if board[2] == 'X': 
            return 1
        else: 
            return 2
    else: 
        return 0


def is_tie(board):
    empty_tiles = [x for x in board if x is None]
    return len(empty_tiles) == 0


def min_max(board,player):
    """Returns optimal move based on the current board.

    Using the Minimax algorithm, finds the optimal move based on the current
    board. Recurses until it finds a game over state (won, lost, or tied) and
    then evaluates the utility of the result (1, -1, or 0, respectively).

    Args:
        board: The list which corresponds to the game board at the moment of
            method call.
        player: A binary value which represents whether X or O is going with 1
            or 0, respectively.

    Returns:
        A tuple which includes the board position which corresponds to the
        optimal move and its utility score.
    """

    if game_won(board) == 1: 
        return (100, -1)
    elif game_won(board) == 2: 
        return (100, 1)
    else:
        if is_tie(board): 
            return (100, 0)
        else:
            play_sign = ''
            if player == 1:
                best_move = (9, 1)
                play_sign = 'X'
            else:
                best_move = (9, -1)
                play_sign = 'O'
            for x in range(9):
                if board[x] is None:
                    board[x] = play_sign
                    min_max_value = (
                        x, min_max(board.copy(), (player + 1) % 2)[1])
                    board[x] = None
                    if player == 1:
                        if min_max_value[1] < best_move[1]: 
                            best_move = min_max_value
                    else:
                        if min_max_value[1] > best_move[1]: 
                            best_move = min_max_value
            return best_move


def main():
    game_board = [None] * 9
    print_board(game_board)
    game_over = False

    while not game_over:
        player_move = int(input('\nPlayer: please pick a free space. '))
        while player_move > 9 or player_move < 1:
            player_move = int(input('Invalid input, please pick a free space between 1 and 9. '))

        while game_board[player_move - 1] is not None: 
            player_move = int(input('Space not free. '))

        game_board[player_move - 1] = 'X'
        if game_won(game_board) == 1:
            print('Congrats, X has won!')
            print_board(game_board)
            break

        if is_tie(game_board):
            print('The game has ended in a tie!')
            print_board(game_board)
            break

        game_board[min_max(game_board, 0)[0]] = 'O'
        print_board(game_board)
        if game_won(game_board) == 2:
            print('Congrats, O has won!')
            game_over = True


if __name__ == '__main__':
    main()
