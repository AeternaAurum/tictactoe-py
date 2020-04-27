from ttt_types import Player
import board
from randombot import RandomBot
from helpers import print_board

import time


def main():
    game = board.GameState.new_game()
    bots = {
        Player.x: RandomBot(),
        Player.o: RandomBot()
    }

    while not game.is_over():
        time.sleep(0.3)
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        game = game.apply_move(bot_move)

    if game.is_over():
        print_board(game.board)
        winner = game.winner()
        winner_str = ''

        if winner is Player.x:
            winner_str = 'X'
        elif winner is Player.o:
            winner_str = 'O'
        else:
            winner_str = 'no one, it\'s a draw!'
        print('Winner is ' + winner_str)


if __name__ == '__main__':
    main()
