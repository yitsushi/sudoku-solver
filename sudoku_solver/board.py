from .error import AmbiguousError


class Board:
    BasicAlphabet = '123456789'

    __field = None
    __alphabet = None

    def __init__(self, alphabet=BasicAlphabet):
        self.__field = [['_'] * len(alphabet)] * len(alphabet)
        self.__alphabet = alphabet
        self.__bs = int(pow(len(alphabet), 0.5))

    def from_file(self, filename, alphabet=BasicAlphabet, separator=','):
        with open(filename) as f:
            self.__field = [
                l.split(separator) for l in f.read().split('\n') if l != ''
            ]

    def field(self):
        return self.__field

    def draw(self):
        [print(" ".join(l)) for l in self.__field]

    def validate(self):
        if self.__bs != pow(len(self.__alphabet), 0.5):
            return False

        if len(self.__field) != len(self.__alphabet):
            return False

        if not all(
            [len(line) == len(self.__alphabet) for line in self.__field]):
            return False

        for i in range(0, len(self.__alphabet)):
            # all uniq in a row
            row = self.__row(i)
            real = [x for x in row if x != '_']
            if len(real) != len(set(real)):
                return False

            # all uniq in a column
            column = self.__column(i)
            real = [x for x in column if x != '_']
            if len(real) != len(set(real)):
                return False

            # all uniq in a block
            block = self.__block(i)
            real = [x for x in block if x != '_']
            if len(real) != len(set(real)):
                return False

        return True

    def solve(self):
        positions = self.__fill_positions()

        tried = 0
        while len(positions) > 0:
            if tried > len(positions):
                raise AmbiguousError(
                    "It's not possible to solve this one or there are more than one solution"
                )
            position = positions.pop(0)

            row = self.__row(self.__row_of(*position))
            column = self.__column(self.__column_of(*position))
            block = self.__block(self.__block_of(*position))

            possible = self.__possible_values(row, column, block)

            if len(possible) == 1:
                tried = 0
                self.__field[position[1]][position[0]] = possible.pop(0)
                continue

            positions.append(position)
            tried += 1

    def __fill_positions(self):
        max_l = len(self.__alphabet)
        return [(i % max_l, i // max_l)
                for i in range(0, pow(len(self.__alphabet), 2))
                if self.__field[i // max_l][i % max_l] == '_']

    def __possible_values(self, row, column, block):
        existing_values = set(row + column + block)
        return [x for x in self.__alphabet if x not in existing_values]

    def __row(self, i):
        return self.__field[i]

    def __column(self, i):
        return [l[i] for l in self.__field]

    def __block(self, i):
        y = (i // 3) * 3
        x = (i % 3) * 3
        return [v for l in self.__field[y:y + 3] for v in l[x:x + 3]]

    def __row_of(self, x, y):
        return y

    def __column_of(self, x, y):
        return x

    def __block_of(self, x, y):
        return ((y // self.__bs) * self.__bs) + (x // self.__bs)
