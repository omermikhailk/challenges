"""A list of functions to help with common themes and tasks in Project Euler
problems, such as: prime factorisation, testing for primality, etc.
"""


from functools import lru_cache
from math import prod


# Prime numbers

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


def sieve_of_eratosthenes(limit: int = 1_000_000) -> list[int]:
    """Uses the Sieve of Eratosthenes algorithm with an arbitary search range
    (`limit`) and generators in Python to yield a prime.

    This could be a lot faster so I'll try my hand at that in the future.

    Args:
        limit (int, optional): The limit that we want to generate primes uptil.

    Returns:
        p [int]: A prime number.
    """
    nums = {i: True for i in range(2, limit + 1) if i % 2}

    yield 2  # Since it's the first prime

    p = 3
    yield p

    while True:
        p_old = p

        # Mark values as False if multiples
        for i in nums.keys():
            if i >= 2 * p and not i % p:
                nums[i] = False

        # Find the new value for `p`
        for i, j in nums.items():
            if i > p and j:
                p = i
                break

        if p == p_old:
            break

        yield p


# Number theory

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


# Sequences and series

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


def main():
    pass


if __name__ == "__main__":
    main()
