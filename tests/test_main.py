from src.main import greet, farewell


def test_greet_basic():
    assert greet("world") == "Hello, world!"


def test_greet_name():
    assert greet("Alice") == "Hello, Alice!"


def test_farewell_basic():
    assert farewell("world") == "Goodbye, world!"


def test_farewell_name():
    assert farewell("Alice") == "Goodbye, Alice!"
