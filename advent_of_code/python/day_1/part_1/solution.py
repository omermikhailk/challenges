def find_increase(file: str) -> int:
    """Given an input, `file`, containing various integer depth values, this
    function will return the number of times that the current depth has
    increased, compared to the previous value.

    Args:
        file (str): The name of the input file.

    Returns:
        tally (int): The number of the times the depth has increased, compared
        to it's previous value.
    """
    tally = 0
    current = 0

    with open(file) as f:
        for num in f:
            if num.strip():
                num = int(num.strip())
                if num > current:
                    if current != 0:
                        tally += 1
                current = num

    return tally


def main():
    print(find_increase("input.txt"))


if __name__ == "__main__":
    main()
