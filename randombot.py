import random
from bot import Bot
from board import Move, BOARD_SIZE
from ttt_types import Point


class RandomBot(Bot):
    def select_move(self, game_state):
        candidates = []
        for r in range(1, BOARD_SIZE + 1):
            for c in range(1, BOARD_SIZE + 1):
                candidate = Point(row=r, col=c)
                if game_state.is_valid_move(Move(candidate)):
                    candidates.append(candidate)
        if not candidates:
            print('Game over')
        return Move(random.choice(candidates))
