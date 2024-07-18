from typing import Optional


def greet(name: Optional[str] = "stranger") -> str:
    return f"Hello, {name}!"


print(greet())
print(greet("Alice"))
