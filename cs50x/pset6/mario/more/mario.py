from cs50 import get_int


def main():
    # Initialize variable to 1
    n = get_int("Height: ")
    # While n is greater than 8 or smaller than 1
    while n > 8 or n < 1:
        # Keep asking user for input
        n = get_int("Height: ")
    # Iterating through a range of 1 to n
    for i in range(1, n + 1):
        # Print the required string on each iteration
        print(" " * (n - i) + "#" * i + "  " + "#" * i)


if __name__ == '__main__':
    main()