"""The really easy way is:

from math import lcm

def equal_divisors(n: int) -> int:
    # Returns the lease commmon divisor of all of the numbers from 1 to `n`.

    # Args:
    #     n (int): The upper limit of the range of numbers we want the LCM for.

    # Returns:
    #     int: The LCM of the numbers from 1 to `n`.

    return lcm(*[i for i in range(1, n + 1)])

However that isn't the point of this challenge
"""


from euler import lcm


def even_divisor(n) -> int:
    """Returns the smallest even divisor (LCM) of the numbers from 1 to `n`.

    Args:
        n (int): The upper bound on the list of numbers we want the LCM for.

    Returns:
        multiple (int): The LCM of all of the numbers from 1 to `n`.
    """
    nums = [i for i in range(1, n + 1)]

    multiple = 0
    for i in range(0, len(nums) - 1):
        if not multiple:
            multiple = lcm(nums[i], nums[i + 1])
        else:
            multiple = lcm(multiple, nums[i + 1])

    return multiple


def main():
    pass


if __name__ == "__main__":
    main()
