from euler import fib


def sum_even_valued(limit: int) -> int:
    """Returns the sum of the even valued terms of the Fibonacci sequence up to
    `limit`.

    Args:
        limit (int): The limit for the values of the terms of the series.

    Returns:
        int: The sum of the even valued terms of the sequence, up to `limit`.
    """
    n = 1
    while fib(n) <= limit:
        n += 1

    return sum([fib(i) for i in range(1, n) if not fib(i) % 2])


def main():
    print(sum_even_valued(4_000_000))


if __name__ == "__main__":
    main()
