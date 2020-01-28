from collections import deque

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

        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append((end_vertex, weight))

    def add_nondirectional_edge(self, start_vertex, end_vertex, weight=0):
        self.add_edge(start_vertex, end_vertex, weight)
        self.add_edge(end_vertex, start_vertex, weight)

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def breadth_first(self, vertex):
        output = []
        def action(vertex):
            output.append(vertex)
        self.__traverse(vertex, action)

        return output

    def __traverse(self, vertex, action):
        q = Queue()
        q.enqueue(vertex)
        visited = set([vertex])
        while not q.empty():
            current = q.dequeue()
            for edge in self.get_neighbors(current):
                v = edge[0]
                if v not in visited:
                    visited.add(v)
                    q.enqueue(v)
            action(current)


class Vertex:
    def __init__(self, value):
        self.value = value

class Queue:
    def __init__(self):
        self.q = deque()


    def enqueue(self, value):
        self.q.appendleft(value)

    def dequeue(self):
        return self.q.pop()

    def empty(self):
        return len(self.q) == 0
