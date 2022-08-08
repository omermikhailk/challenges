def triplet_product(n: int) -> int:
    """Finds the Pythagorean triplets `a`, `b` and `c` which add up to
    `n`, and returrns their product.

    Uses Euclid's formula to generate the triplets.

    Args:
        n (int): The sum that the triplets add up to.

    Returns:
        int: The product of the triplets.
    """
    for i in range(1, n):
        for j in range(i + 1, n):
            a = j ** 2 - i ** 2
            b = 2 * i * j
            c = j ** 2 + i ** 2
            if a + b + c == n:
                return a * b * c


def main():
    print(triplet_product(1000))


if __name__ == "__main__":
    main()
