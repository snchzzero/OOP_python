import random

class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for _ in range(self._length)]
        self._ship_coords = []

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return tuple(self._x, self._y)

    def move(go):
        pass

    def is_collide(self, ship):

        ship_coords_other = [[ship._x, ship._y]]
        for cel in range(1, ship._length):
            if ship._tp == 1:
                ship_coords_other.append([
                    ship_coords_other[-1][0] + 1,
                    ship_coords_other[-1][1]
                ])
            if ship._tp == 2:
                ship_coords_other.append([
                    ship_coords_other[-1][0],
                    ship_coords_other[-1][1] + 1
                ])

        for x, y in self._ship_coords:
            x_l = [y, x - 1]
            xy_lt = [y + 1, x - 1]
            y_t = [y + 1, x]
            xy_rt = [y + 1, x + 1]
            x_r = [y, x + 1]
            xy_rb = [y - 1, x + 1]
            y_b = [y - 1, x]
            xy_lb = [y - 1, x - 1]
        if not all(point not in ship_coords_other for point in [x_l, xy_lt, y_t, xy_rt, x_r, xy_rb, y_b, xy_lb]):
            del self._ship_coords
            return True
        return False

    def is_out_pole(self, size):
        if self._tp == 1:
            if self._x + self._length > size:
                return True
        if self._tp == 2:
            if self._y + self._length > size:
                return True
        return False

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
        for ship in range(-1, -len(self._ships) - 1, -1):
            add_ship = False
            ship = self._ships[ship]
            self.init_ship_coord(ship)
            while add_ship == False:
                collide = False
                for ship_other in self._ships:
                    if ship_other != ship and (ship_other._x != None or ship_other._y != None):
                        if ship.is_collide(ship_other):
                            collide = True
                            break
                if collide:
                    self.init_ship_coord(ship)
                add_ship = True

            # add true coord in main pole
            for x, y in ship._ship_coords:
                self._pole[y][x] = 1









            # add_ship = False
            # ship_coords = self.init_ship_coord(ship)
            #
            # while add_ship is False:
            #     collide = False
            #     for x, y in ship_coords:
            #         collide_one_ship_coord = []
            #         x_l = [y, x - 1] if x - 1 >= 0 else None
            #         xy_lt = [y + 1, x - 1] if x - 1 >= 0 and y + 1 < self._size else None
            #         y_t = [y + 1, x] if y + 1 < self._size else None
            #         xy_rt = [y + 1, x + 1] if y + 1 < self._size and x + 1 < self._size else None
            #         x_r = [y, x + 1] if x + 1 < self._size else None
            #         xy_rb = [y - 1, x + 1] if x + 1 < self._size and y - 1 >= 0 else None
            #         y_b = [y - 1, x] if y - 1 >= 0 else None
            #         xy_lb = [y - 1, x - 1] if x - 1 >= 0 and y - 1 >= 0 else None
            #         for point in [check_point for check_point in [x_l, xy_lt, y_t, xy_rt, x_r, xy_rb, y_b, xy_lb] if
            #                       check_point]:
            #             collide_one_ship_coord.append(self._pole[point[0]][point[1]] == 0)
            #         if not all(collide_one_ship_coord):
            #             ship_coords = self.init_ship_coord(ship)
            #             collide = True
            #             break
            #     if not collide:
            #         add_ship = True

            # add true coord in main pole
            # for x, y in ship_coords:
            #     self._pole[y][x] = 1
            # ship._x = ship_coords[0][0]
            # ship._y = ship_coords[0][1]

    def init_ship_coord(self, ship):
        flag = True
        while flag:
            x_start = random.randrange(0, self._size)
            y_start = random.randrange(0, self._size)
            ship.set_start_coords(x_start, y_start)
            flag = ship.is_out_pole(self._size)



            # if ship._tp == 1:
            #     if not x_start + ship._length > self._size:
            #         flag = False
            # if ship._tp == 2:
            #     if not y_start + ship._length > self._size:
            #         flag = False


        # fill by length, tp
        ship._ship_coords = [[x_start, y_start]]
        for col_coord in range(ship._length - 1):
            if ship._tp == 1:
                x = ship._ship_coords[-1][0] + 1
                y = ship._ship_coords[-1][1]
                ship._ship_coords.append([x, y])
            if ship._tp == 2:
                x = ship._ship_coords[-1][0]
                y = ship._ship_coords[-1][1] + 1
                ship._ship_coords.append([x, y])



    def get_ships(self):
        return self._ships

    def move_ships(self):
        pass

    def show(self):
        show_str = ""
        for row in self._pole:
            show_str += str(row).replace('[', '').replace(']', '') + '\n'
        print(show_str)

    def get_pole(self):
        pass


SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()
pole.show()


