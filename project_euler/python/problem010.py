from euler import sieve_of_eratosthenes


def prime_sum(n: int) -> int:
    """Returns the sum of all of the primes below `n`.

    Args:
        n (int): The limit beyond which we don't want to consider any primes.

    Returns:
        int: The sum of the primes below `n`.
    """
    return sum(sieve_of_eratosthenes(limit=n))


def main():
    print(prime_sum(2_000_000))


if __name__ == "__main__":
    main()
