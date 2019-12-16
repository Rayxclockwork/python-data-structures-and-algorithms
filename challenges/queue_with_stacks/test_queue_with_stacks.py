from queue_with_stacks import Node, Stack, PseudoQueue
import pytest

def test_stack_instance():
    assert Stack()
    

def test_queue_instance():
    assert PseudoQueue()
    

def test_node_instance():
    assert Node(6)
    

def test_push(new_stack):
	new_stack.push(5)
	assert new_stack.top.value == 5

def test_pop(new_stack):
	new_stack.pop()
	assert new_stack.top.value == 18


def test_pseudoqueue_enqueue():
    pseudo = PseudoQueue()
    pseudo.enqueue('Portland')
    pseudo.enqueue('Lawrence')
    pseudo.enqueue('Gladstone')
    expected = 'Portland'
    actual = pseudo.front.value
    assert expected == actual

def test_pseudoqueue_dequeue():
    pseudo = PseudoQueue()
    pseudo.enqueue('Portland')
    pseudo.enqueue('Lawrence')
    pseudo.enqueue('Gladstone')
    expected = 'Portland'
    actual = pseudo.dequeue()
    assert expected == actual

def test_pseudoqueue_enqueue_stack_two_empty():
    pseudo = PseudoQueue()
    pseudo.enqueue('Portland')
    expected = 'Portland'
    actual = pseudo.stack_one.peek()
    assert actual == expected

def test_pseudoqueue_enqueue_stack_one_many():
    pseudo = PseudoQueue()
    pseudo.enqueue('Portland')
    pseudo.enqueue('Lawrence')
    pseudo.enqueue('Gladstone')
    expected = 'Gladstone'
    actual = pseudo.stack_one.peek()
    assert actual == expected

def test_pseudoqueue_dequeue_both_stacks_empty():
    pseudo = PseudoQueue()
    expected = None
    actual = pseudo.dequeue()
    assert actual == expected
	
def test_pseudoqueue_dequeue_both_stacks_many():
    pseudo = PseudoQueue()
    pseudo.enqueue('Portland')
    pseudo.enqueue('Lawrence')
    pseudo.enqueue('Gladstone')
    pseudo.dequeue()
    pseudo.enqueue('Shawnee Mission')
    pseudo.enqueue('Seattle')
    pseudo.enqueue('Kansas City')
    pseudo.dequeue()
    assert pseudo.stack_one.peek() == 'Kansas City'

@pytest.fixture()
def new_stack():
    print('in new list')
    test_stack = Stack()
    for i in range(1, 20):
        test_stack.push(i)
    return test_stack