import pytest

from conjuntos.conjunto3 import kruskall

graph_and_mst = [
    # Case 1: Basic graph with 4 vertices and an MST
    (
        4,
        [(1, 3, 15), (0, 1, 10), (2, 3, 4), (0, 2, 6), (0, 3, 5)],
        {(2, 3, 4), (0, 3, 5), (0, 1, 10)},
    ),
    # Case 2: Simple triangle graph
    (
        3,
        [(0, 1, 1), (1, 2, 2), (0, 2, 3)],
        {(0, 1, 1), (1, 2, 2)},
    ),
    # Case 3: Linear chain
    (
        5,
        [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)],
        {(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)},
    ),
    (
        # Case 4: Complex graph
        9,
        [
            (7, 6, 1),
            (8, 2, 2),
            (6, 5, 2),
            (0, 1, 4),
            (2, 5, 4),
            (8, 6, 6),
            (2, 3, 7),
            (7, 8, 7),
            (0, 7, 8),
            (1, 2, 8),
            (3, 4, 9),
            (5, 4, 10),
            (1, 7, 11),
            (3, 5, 14),
        ],
        {
            (0, 1, 4),
            (0, 7, 8),
            (7, 6, 1),
            (6, 5, 2),
            (2, 5, 4),
            (8, 2, 2),
            (2, 3, 7),
            (3, 4, 9),
        }
    ),
]


@pytest.mark.parametrize("vertices,graph,mst", graph_and_mst)
def test_kruskall(vertices, graph, mst):
    assert set(kruskall(vertices, graph)) == mst
