from graphs import Graph, Vertex
import pytest

def test_add_node():
    graph = Graph()
    actual = graph.add_node('testing').value
    expected = 'testing'
    assert actual == expected

def test_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected


def test_size():
    graph = Graph()
    graph.add_node('testing')
    expected = 1
    actual = graph.size()
    assert actual == expected


def test_add_edge_interloper_start():
    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_add_edge_interloper_end():
    graph  = Graph()
    end = Vertex('end')
    start = graph.add_node('start')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_add_edge_works():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    graph.add_edge(start, end)

def test_add_edge_effect():
    graph = Graph()
    end = graph.add_node('coffee')
    start = graph.add_node('muffin')
    graph.add_edge(start, end)
    expected = (end, 0)
    actual = graph._adjacency_list[start][0]
    assert actual == expected

def test_add_edge_effect_with_weight():
    graph = Graph()
    end = graph.add_node('coffee')
    start = graph.add_node('muffin')
    graph.add_edge(start, end, 44)
    expected = (end, 44)
    actual = graph._adjacency_list[start][0]
    assert actual == expected

def test_get_nodes():
    graph = Graph()
    graph.add_node('coffee')
    graph.add_node('muffin')
    Vertex('loner')
    expected = 2
    actual = len(graph.get_nodes())
    assert actual == expected

def test_get_neighbors():
    graph = Graph()
    end = graph.add_node('coffee')
    start = graph.add_node('muffin')
    graph.add_edge(start, end, 44)
    neighbors = graph.get_neighbors(start)
    assert len(neighbors) == 1
    assert neighbors[0][0].value == 'coffee'
    assert isinstance(neighbors[0][0], Vertex)
    assert neighbors[0][1] == 44

def test_breadth_first():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    g.add_nondirectional_edge(v1, v2, 110)
    expected = ['Pandora', 'Mordor']
    actual = g.breadth_first(v1)
    assert expected == actual


def test_get_edges_one_vertex():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')

    g.add_nondirectional_edge(v1, v2, 110)
    g.add_nondirectional_edge(v2, v3, 50)
    g.add_nondirectional_edge(v2, v4, 12)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)

    actual = g.get_edge(['Mordor'])
    expected = (True, '$0')
    assert actual == expected


def test_get_edges_two_vertex():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')

    g.add_nondirectional_edge(v1, v2, 110)
    g.add_nondirectional_edge(v2, v3, 50)
    g.add_nondirectional_edge(v2, v4, 12)
    g.add_nondirectional_edge(v3, v4, 75)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)

    actual = g.get_edge(['Monstropolis', 'Metroville'])
    expected = (True, '$75')
    assert actual == expected


def test_three_vertex():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')

    g.add_nondirectional_edge(v1, v2, 110)
    g.add_nondirectional_edge(v2, v3, 50)
    g.add_nondirectional_edge(v2, v4, 12)
    g.add_nondirectional_edge(v3, v4, 75)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)

    actual = g.get_edge(['Pandora', 'Mordor', 'Monstropolis'])
    expected = (True, '$160')
    assert actual == expected


def test_false_get_edges():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')

    g.add_nondirectional_edge(v1, v2, 110)
    g.add_nondirectional_edge(v2, v3, 50)
    g.add_nondirectional_edge(v2, v4, 12)
    g.add_nondirectional_edge(v3, v4, 75)
    g.add_nondirectional_edge(v3, v5, 43)
    g.add_nondirectional_edge(v4, v5, 23)
    g.add_nondirectional_edge(v4, v6, 14)
    g.add_nondirectional_edge(v5, v6, 21)

    actual = g.get_edge(['Naboo, Pandora'])
    expected = (False, '$0')
    assert actual == expected


def test_depth_first_1():
    g = Graph()
    v1 = g.add_node('A')
    v2 = g.add_node('B')
    v3 = g.add_node('C')
    v4 = g.add_node('G')
    v5 = g.add_node('D')
    v6 = g.add_node('E')
    v7 = g.add_node('F')
    v8 = g.add_node('H')

    g.add_nondirectional_edge(v1, v2, 110)
    g.add_nondirectional_edge(v2, v3, 50)
    g.add_nondirectional_edge(v2, v5, 12)
    g.add_nondirectional_edge(v3, v4, 75)
    g.add_nondirectional_edge(v1, v5, 43)
    g.add_nondirectional_edge(v5, v7, 23)
    g.add_nondirectional_edge(v7, v8, 14)
    g.add_nondirectional_edge(v5, v6, 21)
    g.add_nondirectional_edge(v5, v8, 29)


    actual = g.depth_first('A')
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert actual == expected
