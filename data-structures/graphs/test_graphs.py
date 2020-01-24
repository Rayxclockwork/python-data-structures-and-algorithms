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
    assert neighbors[0].value == 'coffee'
    assert isinstance(neighbors[0][0], Vertex)
    assert neighbors[0][1] == 44

