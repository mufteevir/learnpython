"""
Create a program which takes a connected, undirected graph with weights and outputs the minimum spanning tree
of the graph i.e., a
subgraph that is a tree, contains all the vertices, and the sum of its weights is the least possible.
"""


# Класс для представления непересекающегося множества
class DisjointSet:
    parent = {}

    # выполняет операцию MakeSet
    def makeSet(self, n):
        # создает `n` непересекающихся наборов (по одному на каждую вершину)
        for i in range(n):
            self.parent[i] = i

    # Найти корень множества, которому принадлежит элемент `k`
    def find(self, k):
        # , если `k` — root
        if self.parent[k] == k:
            return k

        # повторяется для родителя, пока мы не найдем корень
        return self.find(self.parent[k])

    # Выполнить объединение двух подмножеств
    def union(self, a, b):
        # найти корень множеств, которым принадлежат элементы `x` и `y`
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y


# Функция построения MST с использованием алгоритма Крускала
def runKruskalAlgorithm(edges, n):
    # сохраняет ребра, присутствующие в MST.
    MST = []

    # Инициализировать класс DisjointSet.
    # Создайте отдельный набор для каждого элемента вселенной.
    ds = DisjointSet()
    ds.makeSet(n)

    index = 0

    # сортирует края по возрастанию веса
    edges.sort(key=lambda x: x[2])

    # MST содержит точно ребра `V-1`.
    while len(MST) != n - 1:

        # рассматривает следующее ребро с минимальным весом из Graph
        (src, dest, weight) = edges[index]
        index = index + 1

        # найти корень множеств, к которым две конечные точки
        # вершин следующего ребра принадлежит
        x = ds.find(src)
        y = ds.find(dest)
        print(x,y)

        # , если обе конечные точки имеют разных родителей, они принадлежат
        # различные подключаемые компоненты и могут быть включены в MST
        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)

    return MST


if __name__ == '__main__':
    # Триплет # (u, v, w) представляет собой ненаправленное ребро из
    # вершина `u` в вершину `v` с весом `w`
    edges = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]

    # общее количество узлов в Graph (от 0 до 6)
    n = 7

    # Graph построения
    e = runKruskalAlgorithm(edges, n)

    print(e)