from fifo_animal_shelter import Animal, Dog, Cat, AnimalShelter
import pytest


def test_queue_instance():
	queue = AnimalShelter()
	assert queue

def test_animal():
	animal = Animal('cat')
	assert animal

def test_cat():
	cat = Cat()
	assert cat

def test_dog():
	dog = Dog()
	assert dog

def test_animal_caps():
	caps = Animal('DOG')
	assert caps

def test_enqueue():
	empty = AnimalShelter()
	empty.enqueue('cat')
	assert empty.front == 'cat'

def test_enqueue_bad_value():
	with pytest.raises(TypeError):
		Animal('lizard')
