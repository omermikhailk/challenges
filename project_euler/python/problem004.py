def biggest_palindrome(d: int) -> int:
    """Returns the biggest palindrome that can be made from multiplying
    two digits, each of which have `d` number of digits.

    Args:
        d (int): The number of digits each number has.

    Returns:
        int: The biggest plaindrome that can be found from the product of all
        numbers with `d` digits.
    """
    bound_lower = 10 ** (d - 1)
    bound_upper = 10 ** d

    palindromes = []
    for i in range(bound_lower, bound_upper):
        for j in range(i, bound_upper):
            if str(i * j) == str(i * j)[::-1]:
                palindromes.append(i * j)

    return max(palindromes)


def main():
    print(biggest_palindrome(3))


if __name__ == "__main__":
    main()
