def greet(name: str) -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def farewell(name: str) -> str:
    """Return a farewell string."""
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    print(greet("world"))
    print(farewell("world"))
