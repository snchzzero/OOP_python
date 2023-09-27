import random

class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.pole_size = N
        self.pole_col_mine = M
        self.pole = []
        self.init()

    def init(self):
        mines_cords = []
        for _ in range(0, self.pole_col_mine):
            cords = [random.randrange(0, self.pole_size), random.randrange(0, self.pole_size)]
            while cords in mines_cords:
                cords = [random.randrange(0, self.pole_size), random.randrange(0, self.pole_size)]
            mines_cords.append(cords)
        # mines_cords = [[0, 1], [0, 8], [1, 4], [1, 6], [3, 5], [4, 3], [5, 0], [5, 3], [5, 5], [5, 6], [5, 7], [6, 4],
        #                [6, 5], [8, 2]]  # rivert
        # mines_cords = [[0, 2], [2, 4], [2, 5], [3, 0], [3, 3], [3, 5], [3, 6], [3, 7], [4, 3], [5, 5], [7, 4], [7, 6], [8, 1], [8, 8]]

        for row in range(0, self.pole_size):
            column_list = []
            for column in range(0, self.pole_size):
                mine = True if [row, column] in mines_cords else False
                column_list.append(Cell(mine=mine))
            self.pole.append(column_list)

        for y, row in enumerate(self.pole):
            for x, cell in enumerate(row):
                around_mines = 0
                x_l = [y, x-1] if x - 1 >= 0 else None
                xy_lt = [y+1, x-1] if x - 1 >= 0 and y + 1 < self.pole_size else None
                y_t = [y+1, x] if y + 1 < self.pole_size else None
                xy_rt = [y+1, x+1] if y + 1 < self.pole_size and x + 1 < self.pole_size else None
                x_r = [y, x+1] if x + 1 < self.pole_size else None
                xy_rb = [y-1, x+1] if x + 1 < self.pole_size and y - 1 >= 0 else None
                y_b = [y-1, x] if y - 1 >= 0 else None
                xy_lb = [y-1, x-1] if x - 1 >= 0 and y - 1 >= 0 else None
                for point in [check_point for check_point in [x_l, xy_lt, y_t, xy_rt, x_r, xy_rb, y_b, xy_lb] if check_point ]:
                    if self.pole[point[0]][point[1]].mine:
                        around_mines += 1
                cell.around_mines =around_mines

    def show(self):
        pole_string = ''
        for row in range(self.pole_size - 1, 0, -1):
            for cell in self.pole[row]:
                cell_string = '#'
                if cell.fl_open:
                    if cell.mine:
                        cell_string = '*'
                    else:
                        cell_string = f'{cell.around_mines}'
                pole_string += cell_string + ' '
            pole_string += '\n'
        return pole_string


pole_game = GamePole(10, 12)






# print(pole_game.show())
# print(0)
# print(111)

Cell.__doc__

N = 10
M = 10


def get_around_mines(i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or jj < 0 or ii >= N or jj >= N:
                continue
            if pole_game.pole[ii][jj].mine:
                n += 1
    return n


for i in range(N):
    for j in range(N):
        if not pole_game.pole[i][j].mine:
            assert pole_game.pole[i][j].around_mines == get_around_mines(i,
                                                                         j), f"неверное число мин вокруг клетки с индексами {i, j}"

