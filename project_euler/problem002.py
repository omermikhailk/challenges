from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Calculates the `n`-th term of the Fibonacci sequence using recursion.

    This particular sequence varies from the traditional one by starting with 1
    and 2. Leading to:

    `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

    Args:
        n (int): The term of our Fibonacci sequence.

    Returns:
        int: The value of the `n`-th term of the sequence.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


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
