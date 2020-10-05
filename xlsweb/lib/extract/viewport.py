from itertools import product


class Viewport:
    def __init__(self, range):
        tl, br = range.split(':')
        self.top, self.left = self.cell_to_index(tl)
        self.bottom, self.right = self.cell_to_index(br)

    @property
    def row_indexes(self):
        return range(self.top, self.bottom + 1)

    @property
    def col_indexes(self):
        return range(self.left, self.right + 1)

    @property
    def header(self):
        stop = self.right - self.left + 1
        return tuple(self)[:stop]

    @property
    def data(self):
        start = self.right - self.left + 1
        return tuple(self)[start:]

    def __iter__(self):
        yield from product(self.row_indexes, self.col_indexes)

    @staticmethod
    def cell_to_index(cell):
        col = cell[0]
        col = ord(col) - ord('A')
        row = int(cell[1:]) - 1
        return row, col


if __name__ == '__main__':
    assert Viewport.cell_to_index('B3') == (2, 1)
    assert Viewport.cell_to_index('E13') == (12, 4)

    assert Viewport('B3:E13')
    v = Viewport('B3:E13')
    assert (v.top == 2 and v.left == 1 and
            v.bottom == 12 and v.right == 4)

    assert v.row_indexes == range(2, 12 + 1)
    assert v.col_indexes == range(1, 4 + 1)

    assert tuple(v)[:4] == ((2, 1), (2, 2), (2, 3), (2, 4))
    assert tuple(v)[-4:] == ((12, 1), (12, 2), (12, 3), (12, 4))

    assert v.header == ((2, 1), (2, 2), (2, 3), (2, 4))
    assert len(v.data) == 4 * 10
