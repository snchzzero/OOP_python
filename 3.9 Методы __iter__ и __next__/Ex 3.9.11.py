class Matrix:
    def __init__(self, *args):
        if (isinstance(args[0], (int, float))) and \
            all([isinstance(arg, (int, float)) for arg in args]):
                self.rows = args[0]
                self.cols = args[1]
                self.fill_value = args[2]
                self.table = [[self.fill_value for col in range(self.cols)]for row in range(self.rows)]
        elif isinstance(args[0][0], list):
            if self.valid_table(args[0]):
                self.rows = len(args[0])
                self.cols = len(args[0][0])
                self.table = args[0]
        else:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')


    def valid_table(self, list):
        if all([len(l) == len(list[0]) for l in list]):
            if all([all([isinstance(arg[0], (int, float)), isinstance(arg[1], (int, float))]) for arg in list]):
                return True
            else:
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        else:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def valid_index(self, item):
        if all([isinstance(item[0], int) and 0 <= item[0] < self.rows,
               isinstance(item[1], int) and 0 <= item[1] < self.cols]):
            return True
        else:
            raise IndexError('недопустимые значения индексов')

    def valid_data(self, value):
        if isinstance(value, (int, float)):
            return True
        else:
            raise TypeError('значения матрицы должны быть числами')

    def __getitem__(self, item):
        if self.valid_index(item):
            return self.table[item[0]][item[1]]

    def __setitem__(self, key, value):
        if self.valid_index(key) and self.valid_data(value):
            self.table[key[0]][key[1]] = value


    def __add__(self, other):
        if isinstance(other, int):
             return (other + self)
        elif len(self.table[0]) == len(other.table[0]) and len(self.table) == len(other.table):
            list = [[self.table[i][j] + other.table[i][j] for j in range(len(self.table[0]))]for i in range(len(self.table))]
            return Matrix(list)
        else:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __radd__(self, other):
        return Matrix(list(map(lambda x:  [x[0] + other,  x[1] + other], self.table)))

    def __sub__(self, other):
        if isinstance(other, int):
             return (other - self)
        elif len(self.table[0]) == len(other.table[0]) and len(self.table) == len(other.table):
            list = [[self.table[i][j] - other.table[i][j] for j in range(len(self.table[0]))]for i in range(len(self.table))]
            return Matrix(list)
        else:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __rsub__(self, other):
        return Matrix( list(map(lambda x:  [x[0] - other,  x[1] - other], self.table)))

# matrix = Matrix(4, 5, 0)
# matrix2 = Matrix([[1, 2], [3, 4]])
# matrix3 = Matrix([[5, 6], [7, 7]])
# #print(matrix[0, 0]) # возвращается первый элемент матрицы
# matrix[1, 2] = 8 # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
# #print(matrix[1, 2])
# matrix2 + matrix3
# m2 = matrix2 + 10
# matrix4 = matrix3 - matrix2
# matrix5 = matrix3 - 1
# matrix6 = matrix3 - 2

list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"