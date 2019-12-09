import pytest
from diner import Diner


def test_diner_instance():
    diner = Diner()
    assert diner


def test_greeting():

    prints = ['Welcome to TDD Diner',
              'Home of the hottest cup of joe',
              'One order of lasagna with ceaser salad coming up'
              ]
    prompts = ['Enter a Main Dish: ', 'Enter a Side Dish: ']
    responses = ['lasagna', 'ceaser salad']

    def print_for_testing(message):
        if len(prompts):
            assert message == prints.pop(0)

    def input_for_testing(prompt):
        if len(prompts):
            assert prompt == prompts.pop(0)

    diner = Diner(print_for_testing, input_for_testing)
    diner.dine()
