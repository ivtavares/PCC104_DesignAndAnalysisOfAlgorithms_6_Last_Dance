from typing import List, Tuple


weight = float
origin_vertex = int
destination_vertex = int

Edge = Tuple[origin_vertex, destination_vertex, weight]


class UnionFind:
    def __init__(self, vertices: int):
        self.parent = list(range(vertices))  # Inicialmente, cada nó é seu próprio pai
        self.rank = [0] * vertices  # Inicializa o rank com 0 para todos os nós

    # Operação Find com Compressão de Caminho
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Caminho encurtado
        return self.parent[x]

    # Operação Union com Union by Rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1


def kruskall(vertices: int, edges: List[Edge]) -> List[Edge]:
    edges = sorted(edges, key=lambda edge: edge[2])
    mst: List[Edge] = list()
    uf = UnionFind(vertices)
    counter = 0

    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            counter += 1
        if counter > vertices - 1:
            break
    return mst
