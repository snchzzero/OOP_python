import random

class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for _ in range(self._length)]
        self.ship_coords = []

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y


    def get_start_coords(self):
        return tuple(self._x, self._y)

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x = self._x + go
            elif self._tp == 2:
                self._y = self._y + go



    def is_collide(self, ship):

        for x, y in self.ship_coords:
            x_l = [y, x - 1]
            xy_lt = [y + 1, x - 1]
            y_t = [y + 1, x]
            xy_rt = [y + 1, x + 1]
            x_r = [y, x + 1]
            xy_rb = [y - 1, x + 1]
            y_b = [y - 1, x]
            xy_lb = [y - 1, x - 1]
            if not all([point[1], point[0]] not in ship.ship_coords for point in [[y, x], x_l, xy_lt, y_t, xy_rt, x_r, xy_rb, y_b, xy_lb]):
                del self.ship_coords
                return True
        return False

    def is_out_pole(self, size):
        if self._tp == 1:
            if self._x + self._length > size or self._x < 0:
                return True
        if self._tp == 2:
            if self._y + self._length > size or self._y < 0:
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
                else:
                    add_ship = True

            # add true coord in main pole
            for x, y in ship.ship_coords:
                self._pole[y][x] = 1


    def init_ship_coord(self, ship, x_start=None, y_start=None):
        flag = True
        if x_start is None and y_start is None:
            while flag:
                x_start = random.randrange(0, self._size)
                y_start = random.randrange(0, self._size)
                ship.set_start_coords(x_start, y_start)
                flag = ship.is_out_pole(self._size)

        if x_start and y_start:
            ship.set_start_coords(x_start, y_start)
            if ship.is_out_pole(self._size):
                return True

        # fill by length, tp
        ship.ship_coords = [[x_start, y_start]]
        for col_coord in range(ship._length - 1):
            if ship._tp == 1:
                x = ship.ship_coords[-1][0] + 1
                y = ship.ship_coords[-1][1]
                ship.ship_coords.append([x, y])
            if ship._tp == 2:
                x = ship.ship_coords[-1][0]
                y = ship.ship_coords[-1][1] + 1
                ship.ship_coords.append([x, y])



    def get_ships(self):
        return self._ships

    def move_ships(self):
        mover_ship = []
        for ship in self._ships:
            forward_backward = random.choice([-1, 1])
            old_x = ship._x
            old_y = ship._y
            old_ship_coords = ship.ship_coords
            #flag = True
            for trying_move in [forward_backward, forward_backward * -1]:
                flag = True
                if ship._tp == 1:
                    new_x = old_x + trying_move
                    new_y = old_y
                elif ship._tp == 2:
                    new_x = old_x
                    new_y = old_y + trying_move
                if self.init_ship_coord(ship, x_start=new_x, y_start=new_y):
                    self.init_ship_coord(ship, x_start=old_x, y_start=old_y)
                    flag = False
                    continue

                result_collid = []

                for other_ship in self._ships:

                    if ship != other_ship:
                        if ship.is_collide(other_ship):
                            self.init_ship_coord(ship, x_start=old_x, y_start=old_y)
                            flag = False
                            break

                if not flag:
                    continue

                if flag:  # если успешно переместили на клетку
                    for old_ship_x, old_ship_y in old_ship_coords:

                        self._pole[old_ship_y][old_ship_x] = 0
                    for new_ship_x, new_ship_y in ship.ship_coords:
                        self._pole[new_ship_y][new_ship_x] = 1
                    mover_ship.append(ship)
                    break

            if not flag:
                mover_ship.append(ship)
                self.init_ship_coord(ship, x_start=old_x, y_start=old_y)
                continue







    def show(self):
        show_str = ""
        for row in self._pole:
            show_str += str(row).replace('[', '').replace(']', '').replace(',', ' ') + '\n'
        print(show_str)

    def get_pole(self):
        pass


SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()
pole.move_ships()
pole.show()
pole.show()



