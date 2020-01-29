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
            output.append(vertex.value)
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

    def get_edge(self, v_lst):

        def contains_vertex(value, lst):
            for vertex in lst:
                if isinstance(vertex, tuple):
                    if vertex[0].value == value:
                        return vertex
                    continue
                if vertex.value == value:
                    return vertex
            return False, 0

        current = contains_vertex(v_lst[0], self._adjacency_list.keys())
        if isinstance(current, Vertex):
            tsum = 0
            for index in range(1, len(v_lst)):
                current, cost = contains_vertex(v_lst[index], self.get_neighbors(current))
                tsum += cost
                if not current:
                    return (False, '$0')
            return (True, f'${tsum}')
        return (False, '$0')


    def depth_first(self, root):
        lst = []
        s = Stack()
        s.push(root)
        lst.append(root)
        while s:
            vertex = s.pop()
            lst.append(vertex)

            for neighbor in reversed(self.get_neighbors(vertex)):
                if not neighbor[0].visited:
                    vertex.visited = True
                    neighbor[0].visited = True

                    s.push(neighbor[0])

        for node in self._adjacency_list:
            node.visited = False

        return lst

class Vertex:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        """creates new stack instance"""
        self.top = None

    def push(self, value):
        """pushes new node onto stack"""
        new_node = Vertex(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        """takes top node off stack"""
        if self.top == None:
            return ('stack is empty')
        else:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.value

    def peek(self):
        """returns value of top node"""
        return self.top.value

    def is_empty(self):
        """returns boolean stating whether or not stack is empty"""
        if self.top == None:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, value):
        self.q.appendleft(value)

    def dequeue(self):
        return self.q.pop()

    def empty(self):
        return len(self.q) == 0
