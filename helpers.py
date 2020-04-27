import ttt_types
from board import BOARD_SIZE

SYMBOL_TO_STRING = {
    None: ' . ',
    ttt_types.Player.x: ' x ',
    ttt_types.Player.o: ' o ',
}


def print_board(board):
    for row in range(BOARD_SIZE, 0, -1):
        bump = " "
        line = []
        for col in range(1, BOARD_SIZE + 1):
            p = board.get(ttt_types.Point(row=row, col=col))
            line.append(SYMBOL_TO_STRING[p])
        print('%s%d %s' % (bump, row, ''.join(line)))
    print('\n')
