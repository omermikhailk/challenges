"""A list of functions to help with common themes and tasks in Project Euler
problems, such as: prime factorisation, testing for primality, etc.
"""


from functools import lru_cache
from math import prod


def trial_division(n: int) -> list[int]:
    """Returns the prime factors of `n` using the trial division method.

    Args:
        n (int): The number we want the prime factors of.

    Returns:
        prime_factors (list[int]): The list of the prime factors of `n`.
    """
    prime_factors = []
    i = 2

    while n != 1:
        if not n % i:
            prime_factors.append(i)
            n /= i
        else:
            i += 1

    return prime_factors


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


def lcm(a: int, b: int) -> int:
    """Returns the LCM of two numbers, `a` and `b`.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The LCM of `a` and `b`.
    """
    return abs(a * b) // gcd(a, b)


def gcd(a: int, b: int) -> int:
    """Returns the  GCD of two numbers, `a` and `b`.

    Args:
        a (int): The first number
        b (int): The secnond number

    Returns:
        int: The GCD of `a` and `b`.
    """
    a_factors = trial_division(a)
    b_factors = trial_division(b)

    divisor = []
    for i in a_factors:
        if i in b_factors:
            b_factors.remove(i)
            divisor.append(i)

    return prod(divisor)


def main():
    pass


if __name__ == "__main__":
    main()