# test_main.py
from main import greet, add_numbers

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("AI") == "Hello, AI!"

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0