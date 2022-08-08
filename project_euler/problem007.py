from euler import sieve_of_eratosthenes


def get_prime(n: int) -> int:
    for index, prime in enumerate(sieve_of_eratosthenes(), 1):
        if index == n:
            return prime


def main():
    print(get_prime(10001))


if __name__ == "__main__":
    main()
