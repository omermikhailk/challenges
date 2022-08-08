def find_increase_trio(file: str) -> int:
    """Given an input, `file`, containing various integer depth values, this
    function will return the number of times that the sum of a triplet of
    depths (n, n + 1, n + 2) has increased, compared to it's previous value.

    Args:
        file (str): The name of the input file.

    Returns:
        tally (int): The number of the times the sum of a triplet of depths has
        increased, compared to it's previous value.
    """
    tally = 0
    current = 0

    with open(file) as f:
        numbers = f.readlines()

        # Clean-up
        for i in range(len(numbers)):
            if not numbers[i].strip():
                del numbers[i]
            else:
                numbers[i] = int(numbers[i])

        for i in range(0, len(numbers) - 2):
            group = numbers[i:i + 3]
            if sum(group) > current:
                if current != 0:
                    tally += 1
            current = sum(group)

    return tally


def main():
    print(find_increase_trio('input.txt'))


if __name__ == "__main__":
    main()
