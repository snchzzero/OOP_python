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

    def get_link_v(self, v, D):
        for i, weight in enumerate(v.links):
            if weight.dist > 0:
                yield i

    def matrix(self, start_v, stop_v):
        N = len(self._links)  # число вершин в графе
        T = [math.inf] * N  # последняя строка таблицы

        v = start_v  # стартовая вершина (нумерация с нуля)
        S = {v}  # просмотренные вершины
        T[v] = 0  # нулевой вес для стартовой вершины
        M = [0] * N  # оптимальные связи между вершинами

        while v != -1:  # цикл, пока не просмотрим все вершины
            for j in self.get_link_v(v):  # перебираем все связанные вершины с вершиной v
                if j not in S:  # если вершина еще не просмотрена
                    w = T[v] + self._vertex[v][j]
                    if w < T[j]:
                        T[j] = w
                        M[j] = v  # связываем вершину j с вершиной v

            v = arg_min(T, S)  # выбираем следующий узел с наименьшим весом
            if v >= 0:  # выбрана очередная вершина
                S.add(v)  # добавляем новую вершину в рассмотрение

        print(T)




        pass



    def find_path(self, start_v, stop_v):
        matrix = self.matrix(start_v, stop_v)
        pass



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

print(len(map_metro._links))
print(len(map_metro._vertex))
#path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
#print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
#print(sum([x.dist for x in path[1]]))  # 7