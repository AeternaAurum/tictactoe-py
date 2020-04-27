import enum
from collections import namedtuple


class Player(enum.Enum):
    x = 1
    o = 2

    @property
    def other(self):
        return Player.x if self == Player.o else Player.o

    def __str__(self):
        return 'X' if self == Player.x else 'O'

    def __repr__(self):
        return 'X' if self == Player.x else 'O'


class Point(namedtuple('Point', 'row col')):
    def __deepcopy__(self, memodict={}):
        return self
