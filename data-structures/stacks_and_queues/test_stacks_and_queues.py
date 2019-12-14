from stacks_and_queues import Node, Stack, Queue
import pytest

def test_stack_instance():
    stack = Stack()
    assert stack

def test_queue_instance():
    queue = Queue()
    assert queue

def test_node_instance():
    node = Node(6)
    assert node

def test_push(new_stack):
    new_stack.push(21)
    assert new_stack.top.value == 21

def test_pop(new_stack):
    assert new_stack.pop()

def test_stack_peek(new_stack):
    assert new_stack.peek()

def test_stack_is_empty(new_stack):
    expected = False
    actual = new_stack.is_empty()
    assert expected == actual

def test_enqueue():
    empty_queue = Queue()
    empty_queue.enqueue(7)
    assert empty_queue.front.value == 7

def test_dequeue(new_queue):
    assert new_queue.dequeue()

def test_queue_peek(new_queue):
    assert new_queue.peek()

def test_queue_is_empty(new_queue):
    expected = False
    actual = new_queue.is_empty()
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
