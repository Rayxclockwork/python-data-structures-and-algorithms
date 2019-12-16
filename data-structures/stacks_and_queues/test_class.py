from stacks_and_queues import Node, Stack, Queue
import pytest

from stacks_and_queues import Node, Stack, Queue

import pytest

# ========
# FIXTURES
# ========

@pytest.fixture
def node():
    return Node(42)

@pytest.fixture
def stack():
    return Stack()

@pytest.fixture
def full_stack(stack):
    stack.push(42)
    stack.push('October')
    stack.push('Pinhead')
    return stack

@pytest.fixture
def queue():
    return Queue()

@pytest.fixture
def full_queue(queue):
    queue.enqueue(42)
    queue.enqueue('October')
    queue.enqueue('Pinhead')
    return queue

# =====
# TESTS
# =====

def test_node_next(node):
    assert node.next == None

def test_node_value(node):
    assert node.value == 42

def test_empty_stack(stack):
    # Can successfully instantiate an empty stack
    assert stack.top == None
    assert stack.is_empty() == True

def test_stack_push(stack):
    # Can successfully push onto a stack
    assert stack.is_empty() == True
    stack.push(42)
    assert stack.top.value == 42
    assert stack.is_empty() == False

    # Can successfully push multiple values onto a stack
    stack.push('October')
    assert stack.top.value == 'October'
    assert stack.top.next.value == 42
    assert stack.is_empty() == False

def test_stack_peek(full_stack):
    # Can successfully peek the next item on the stack
    assert full_stack.peek() == 'Pinhead'

    full_stack.pop()
    assert full_stack.peek() == 'October'

    full_stack.pop()
    assert full_stack.peek() == 42

    full_stack.pop()
    assert full_stack.peek() == None
    assert full_stack.is_empty() == True

def test_stack_pop(full_stack):
    # Can successfully pop off the stack
    assert full_stack.pop() == 'Pinhead'

    # Can successfully empty a stack after multiple pops
    assert full_stack.pop() == 'October'
    assert full_stack.pop() == 42
    assert full_stack.top == None
    assert full_stack.is_empty() == True

    # Can return None is stack is already empty
    assert full_stack.pop() == None

def test_empty_queue(queue):
    # Can successfully instantiate an empty queue
    assert queue.front == None
    assert queue.is_empty() == True

def test_enqueue_queue(queue):
    # Can successfully enqueue into a queue
    assert queue.is_empty() == True
    queue.enqueue(42)
    assert queue.front.value == 42
    assert queue.is_empty() == False

    # Can successfully enqueue multiple values into a queue
    queue.enqueue('October')
    queue.enqueue('Pinhead')
    assert queue.front.value == 42
    assert queue.front.next.value == 'October'
    assert queue.front.next.next.value == 'Pinhead'
    assert queue.is_empty() == False

def test_dequeue_queue(full_queue):
    # Can successfully dequeue out of a queue the expected value
    assert full_queue.dequeue() == 42

    # Can successfully empty a queue after multiple dequeues
    assert full_queue.dequeue() == 'October'
    assert full_queue.dequeue() == 'Pinhead'
    assert full_queue.front == None
    assert full_queue.is_empty() == True

    # Can return None if the stack is empty
    assert full_queue.dequeue() == None

def test_queue_peek(full_queue):
    # Can successfully peek into a queue, seeing the expected value
    assert full_queue.peek() == 42

    full_queue.dequeue()
    assert full_queue.peek() == 'October'

    full_queue.dequeue()
    assert full_queue.peek() == 'Pinhead'

    full_queue.dequeue()
    assert full_queue.peek() == None
