def sum_of_multiples(num: int) -> int:
    """Goes from 1 to (`num` - 1) and returns the sum of all of the multiples
    of 3 and 5.

    Args:
        num (int): The limit for the range of numbers that we're looking at.

    Returns:
        int: The sum of all of the multiples of 3 and 5 in the
        considered range.
    """
    return sum([i for i in range(1, num) if not i % 3 or not i % 5])


def main():
    print(sum_of_multiples(1000))


if __name__ == "__main__":
    main()
