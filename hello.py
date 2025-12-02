def greet(name: str, capitalize: bool = False) -> str:
    if capitalize:
        name = name.title()
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("world", capitalize=True))
