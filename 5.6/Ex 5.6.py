import random

class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for _ in range(self._length)]

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return tuple(self._x, self._y)

    def move(go):
        pass

    def is_collide(ship):
        pass

    def is_out_pole(size):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, item, value):
        pass


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self._pole = [[0 for column in range(size)] for row in range(size)]

    def init(self):
        # initialize length of ships
        for col_ship in range(10):
            if col_ship in [4, 5, 6]:
                length = 2
            elif col_ship in [7, 8]:
                length = 3
            elif col_ship == 9:
                length = 4
            else:
                length = 1
            self._ships.append(Ship(length, tp=random.randint(1, 2)))

        # initialization coords of ships
        for ship in range(-1, -len(self._ships), -1):
            ship = self._ships[ship]
            add_ship = False
            ship_coords = self.init_ship_coord(ship)

            while add_ship is False:
                collide = False
                for x, y in ship_coords:
                    collide_one_ship_coord = []
                    x_l = [y, x - 1] if x - 1 >= 0 else None
                    xy_lt = [y + 1, x - 1] if x - 1 >= 0 and y + 1 < self._size else None
                    y_t = [y + 1, x] if y + 1 < self._size else None
                    xy_rt = [y + 1, x + 1] if y + 1 < self._size and x + 1 < self._size else None
                    x_r = [y, x + 1] if x + 1 < self._size else None
                    xy_rb = [y - 1, x + 1] if x + 1 < self._size and y - 1 >= 0 else None
                    y_b = [y - 1, x] if y - 1 >= 0 else None
                    xy_lb = [y - 1, x - 1] if x - 1 >= 0 and y - 1 >= 0 else None
                    for point in [check_point for check_point in [x_l, xy_lt, y_t, xy_rt, x_r, xy_rb, y_b, xy_lb] if
                                  check_point]:
                        collide_one_ship_coord.append(self._pole[point[0]][point[1]] is 0)
                    if not all(collide_one_ship_coord):
                        ship_coords = self.init_ship_coord(ship)
                        collide = True
                        break
                if not collide:
                    add_ship = True

            # add true coord in main pole
            for x, y in ship_coords:
                self._pole[y][x] = 1

    def init_ship_coord(self, ship):
        flag = True
        while flag:
            x_start = random.randrange(0, self._size)
            y_start = random.randrange(0, self._size)
            if ship._tp == 1:
                if not x_start + ship._length > self._size:
                    flag = False
            if ship._tp == 2:
                if not y_start + ship._length > self._size:
                    flag = False

        ship_coords = [[x_start, y_start]]

        # random add fill by length, tp
        for col_coord in range(ship._length - 1):
            if ship._tp == 1:
                x = ship_coords[-1][0] + 1
                y = ship_coords[-1][1]
                ship_coords.append([x, y])
            if ship._tp == 2:
                x = ship_coords[-1][0]
                y = ship_coords[-1][1] + 1
                ship_coords.append([x, y])

        return ship_coords









    def get_ships(self):
        return self._ships

    def move_ships(self):
        pass

    def show(self):
        pass

    def get_pole(self):
        pass


SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()


