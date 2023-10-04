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
        if self._x is not None and self._y is not None:
            self.fill_by_length()

    def fill_by_length(self):
        self.ship_coords = [[self._x, self._y]]
        for col_coord in range(self._length - 1):
            if self._tp == 1:
                x = self.ship_coords[-1][0] + 1
                y = self.ship_coords[-1][1]
                self.ship_coords.append([x, y])
            if self._tp == 2:
                x = self.ship_coords[-1][0]
                y = self.ship_coords[-1][1] + 1
                self.ship_coords.append([x, y])


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

    @property
    def tp(self):
        return self._tp

    @tp.setter
    def tp(self, val):
        self._tp = val

    def get_start_coords(self):
        return tuple((self._x, self._y))

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
        return self._cells[item]

    def __setitem__(self, item, value):
        if value == 2:
            self._is_move = False
        self._cells[item] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self._pole = [[0 for column in range(size)] for row in range(size)]

    def refresh_tp(self):
        for ship in self._ships:
            ship._tp = random.randint(1, 2)

    def refresh_x_y(self):
        for ship in self._ships:
            ship._x = None
            ship._y = None



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
        total = 15
        tryin_again = True
        while tryin_again:
            self._pole = [[0 for column in range(self._size)] for row in range(self._size)]
            trying = 0
            get_opt_coord = []
            for ship in range(-1, -len(self._ships) - 1, -1):
                trying = 0
                add_ship = False
                ship = self._ships[ship]

                # новая оптимизация
                if self._size < 9 and ship._length in [3, 4]:
                    start_opt_coord_tp1 = [[0, 0], [0, self._size-1], [self._size - 4, 0], [self._size - 4, self._size-1]]
                    start_opt_coord_tp2 = [[0, 0], [self._size-1, 0], [0, self._size - 4], [self._size-1, self._size - 4]]
                    get_opt_coord_flag = False
                    while not get_opt_coord_flag:
                        if ship._tp == 1:
                            coord = random.choice(start_opt_coord_tp1)
                        if ship._tp == 2:
                            coord = random.choice(start_opt_coord_tp2)
                        if not coord in get_opt_coord:
                            get_opt_coord.append(coord)
                            get_opt_coord_flag = True
                    self.init_ship_coord(ship, coord[0], coord[1])
                else:
                    self.init_ship_coord(ship)


                while add_ship == False and trying < total:
                    collide = False
                    for ship_other in self._ships:
                        if ship_other != ship and (ship_other._x != None or ship_other._y != None):
                            if ship.is_collide(ship_other):
                                del ship.ship_coords
                                collide = True
                                break

                    if collide:
                        if self._size < 9 and ship._length in [3, 4]:
                            start_opt_coord_tp1 = [[0, 0], [0, self._size - 1], [self._size - 4, 0],
                                                   [self._size - 4, self._size - 1]]
                            start_opt_coord_tp2 = [[0, 0], [self._size - 1, 0], [0, self._size - 4],
                                                   [self._size - 1, self._size - 4]]
                            get_opt_coord_flag = False
                            while not get_opt_coord_flag:
                                if ship._tp == 1:
                                    coord = random.choice(start_opt_coord_tp1)
                                if ship._tp == 2:
                                    coord = random.choice(start_opt_coord_tp2)
                                if not coord in get_opt_coord:
                                    get_opt_coord.append(coord)
                                    get_opt_coord_flag = True
                            self.init_ship_coord(ship, coord[0], coord[1])
                        else:
                            self.init_ship_coord(ship)
                        trying += 1
                    if not collide and trying < total:
                        add_ship = True

                    if add_ship and trying < total:
                        # add true coord in main pole
                        for x, y in ship.ship_coords:
                            self._pole[y][x] = 1
                if not add_ship:
                    tryin_again = True
                    self.refresh_tp()
                    self.refresh_x_y()
                    break
            if add_ship:
                tryin_again = False



    def init_ship_coord(self, ship, x_start=None, y_start=None):
        flag = True
        if x_start is None and y_start is None:
            while flag:
                x_start = random.randrange(0, self._size)
                y_start = random.randrange(0, self._size)
                ship.set_start_coords(x_start, y_start)
                flag = ship.is_out_pole(self._size)

        if x_start != None and y_start != None:
            ship.set_start_coords(x_start, y_start)
            if ship.is_out_pole(self._size):
                return True

        ship.fill_by_length()

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
                            del ship.ship_coords
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
        self._pole = [[0 for column in range(self._size)] for row in range(self._size)]
        for ship in self._ships:
            for index, (x, y) in enumerate(ship.ship_coords):
                val = ship._cells[index]
                self._pole[y][x] = val
        for row in self._pole:
            show_str += str(row).replace('[', '').replace(']', '').replace(',', ' ') + '\n'
        print(show_str)

    def get_pole(self):
        result = []
        self._pole = [[0 for column in range(self._size)] for row in range(self._size)]
        for ship in self._ships:
            for index, (x, y) in enumerate(ship.ship_coords):
                val = ship._cells[index]
                self._pole[y][x] = val
        for index, row in enumerate(self._pole):
            result.append(tuple((row)))
        return tuple(result)


# SIZE_GAME_POLE = 10
#
# pole = GamePole(SIZE_GAME_POLE)
# pole.init()
# pole.show()
# pole.move_ships()
# pole.show()
# pole.show()

ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
a = ship.get_start_coords()
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

#res = s1.is_collide(s2)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(7)
pole_size_8.init()
pole_size_8.show()
print('dsfgsssssssssssssssssssssssssssssss')

