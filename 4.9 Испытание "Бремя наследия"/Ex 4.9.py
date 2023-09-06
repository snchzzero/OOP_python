import math


class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist
        self.add_link_vertex()

    def add_link_vertex(self):
        if self not in self._v1._links:
            self._v1._links.append(self)
        if self not in self._v2._links:
            self._v2._links.append(self)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
            if v not in self._vertex:
                self._vertex.append(v)

    def add_link(self, link):

        if all([link.v1 not in v1v2 or link.v2 not in v1v2 for v1v2 in [[lnk.v1, lnk.v2] for lnk in self._links]]):
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def get_index(self, vertex):
        for index, vertex_iter in enumerate(self._vertex):
            if vertex_iter == vertex:
                return index # стартовая вершина (нумерация с нуля)
        return 0

    def arg_min(self, T, S):
        amin = -1
        m = max(T)  # максимальное значение в T (для упрощения алгоритма)
        for index, t in enumerate(T):
            if t < m and self._vertex[index] not in S.values():
                m = t
                amin = index

        return amin

    def matrix(self, start_v, stop_v):
        N = len(self._vertex)  # число вершин в графе
        T = [math.inf] * N  # последняя строка таблицы

        v = self.get_index(start_v)  # стартовая вершина (нумерация с нуля)
        S = {v: self._vertex[v]}  # просмотренные вершины
        T[v] = 0  # нулевой вес для стартовой вершины
        M = [0] * N  # оптимальные связи между вершинами

        while v != -1:  # цикл, пока не просмотрим все вершины
            for j in self._vertex[v].links:  # перебираем все связанные вершины с вершиной v
                if j.v2 not in S.values():  # если вершина еще не просмотрена
                    w = T[v] + j.dist
                    index_j = self.get_index(j.v2)
                    if w < T[index_j]:
                        T[index_j] = w
                        M[index_j] = v  # связываем вершину j с вершиной v
                if j.v1 not in S.values():
                    w = T[v] + j.dist
                    index_j = self.get_index(j.v1)
                    if w < T[index_j]:
                        T[index_j] = w
                        M[index_j] = v
            v = self.arg_min(T, S)  # выбираем следующий узел с наименьшим весом
            if v >= 0:  # выбрана очередная вершина
                #S.add(v)  # добавляем новую вершину в рассмотрение
                S[v] = self._vertex[v]

        print(T)  # [0, 1, 1, 4, 5, 7, 6]

        # формирование оптимального маршрута:
        start = self.get_index(start_v)
        end = self.get_index(stop_v)
        P = [end]
        while end != start:
            end = M[P[-1]]
            P.append(end)
        P.reverse()

        print(P)  # [5, 6, 1, 0] -> [0, 1, 6, 5]
        return P





    def find_path(self, start_v, stop_v):
        shotest_way_index = self.matrix(start_v, stop_v)
        stations = [self._vertex[index] for index in shotest_way_index]
        #print('stations ', stations)
        links = []
        for index in range(0, len(shotest_way_index)):
            if index + 1 != len(shotest_way_index):
                v1 = shotest_way_index[index]
                v1_obj = self._vertex[v1]
                v2 = shotest_way_index[index + 1]
                v2_obj = self._vertex[v2]
                for link in v1_obj.links:
                    if (link.v1 == v1_obj and link.v2 == v2_obj) or (link.v1 == v2_obj and link.v2 == v1_obj):
                        links.append(link)
                        break
        result = (stations, links)
        return result









class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)



# map_graph = LinkedGraph()
#
# v1 = Vertex()
# v2 = Vertex()
# v3 = Vertex()
# v4 = Vertex()
# v5 = Vertex()
# v6 = Vertex()
# v7 = Vertex()
#
# map_graph.add_link(Link(v1, v2))
# map_graph.add_link(Link(v2, v3))
# map_graph.add_link(Link(v1, v3))
#
# map_graph.add_link(Link(v4, v5))
# map_graph.add_link(Link(v6, v7))
#
# map_graph.add_link(Link(v2, v7))
# map_graph.add_link(Link(v3, v4))
# map_graph.add_link(Link(v5, v6))
#
# print(len(map_graph._links))   # 8 связей
# print(len(map_graph._vertex))  # 7 вершин
# path = map_graph.find_path(v1, v6)


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))  # 8 связей
print(len(map_metro._vertex))  # 7 вершин
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7