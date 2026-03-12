"""Core module for the pen example project."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def main() -> None:
    """Simple CLI entry for demonstration."""
    result = add(1, 2)
    print(f"1 + 2 = {result}")


if __name__ == "__main__":
    main()
