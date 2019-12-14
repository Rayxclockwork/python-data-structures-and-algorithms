from stacks_and_queues import Node, Stack, Queue
import pytest

def test_stack_instance():
    stack = Stack()
    assert stack

def test_queue_instance():
    queue = Queue()
    assert queue

def test_node_instance(value):
    node = Node(value)
    assert node

def test_push(test_stack):
    test_stack.push(21)
    assert test_stack.top.value == 21

def test_pop(test_stack):
    assert test_stack.pop(0)

def test_stack_peek(test_stack):
    assert test_stack.peek()

def test_stack_is_empty(self):
    expected = False
    actual = self.top != None
    assert expected == actual

def test_enqueue(test_queue):
    assert test_queue.enqueue()

def test_dequeue(test_queue):
    assert test_queue.dequeue()

def test_queue_peek(test_queue):
    assert test_queue.peek()

def test_queue_is_empty(self):
    expected = True
    actual = self.front == None
    assert expected == actual

@pytest.fixture()
def new_stack():
    print('in new list')
    test_stack = Stack()
    for i in range(1, 20):
        test_stack.push(i)
    return test_stack

@pytest.fixture()
def new_queue():
    print('in new list')
    test_queue = Queue()
    for i in range(1, 20):
        test_queue.enqueue(i)
    return test_queue
