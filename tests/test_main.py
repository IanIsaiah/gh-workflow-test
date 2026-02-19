from src.main import greet


def test_greet_basic():
    assert greet("world") == "Hello, world!"


def test_greet_name():
    assert greet("Alice") == "Hello, Alice!"
