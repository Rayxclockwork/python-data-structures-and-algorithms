class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """Adds a vertex"""

        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def size(self):
        """returns number of values in adjacency list"""

        return len(self._adjacency_list)


    def add_edge(self, start_vertex, end_vertex, weight=0):

        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in graph')

        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in graph')

        # TODO: Handle weight
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append((end_vertex, weight))


    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]


class Vertex:
    def __init__(self, value):
        self.value = value
