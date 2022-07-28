def trial_division(n: int) -> list[int]:
    """Returns the prime factors of `n`.

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


def main():
    print(max(trial_division(600851475143)))


if __name__ == "__main__":
    main()
