from euler import sieve_of_eratosthenes


def get_prime(n: int) -> int:
    """Generates the `n`-th prime and returns it.

    Args:
        n (int): The `n`-th prime that we want.

    Returns:
        int: The value of the `n`-th prime.
    """
    for index, prime in enumerate(sieve_of_eratosthenes(), 1):
        if index == n:
            return prime


def main():
    print(get_prime(10001))


if __name__ == "__main__":
    main()
