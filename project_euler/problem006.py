def sum_square_diff(n: int) -> int:
    """Returns the difference between the square of the sum of the numbers from
    1 to `n` and the sum of the squares of the numbers from 1 to `n`.

    Args:
        n (int): The upper bound of the list of the numbers that are being
        considered.

    Returns:
        int: The difference between the square of the sum and the sum of the
        squares.
    """
    nums = [i for i in range(1, n + 1)]
    return sum(nums) ** 2 - sum([i ** 2 for i in nums])


def main():
    pass


if __name__ == "__main__":
    main()
