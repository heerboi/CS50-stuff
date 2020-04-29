from cs50 import get_string


def main():
    # Obtain number as string
    number = get_string("Number: ")
    # Length of the number
    c = len(number)
    # List of every second element from the second element from the end multiplied by 2 if the product is smaller than 10
    a = [int(number[i]) * 2 for i in range(c - 2, -1, -2) if int(number[i]) * 2 < 10]
    # List of sums of every digit of element whose product is greater than 10
    d = [sum([int(f) for f in str(int(number[i]) * 2)]) for i in range(c - 2, -1, -2) if int(number[i]) * 2 >= 10]
    # List of every other element in the number
    b = [int(number[i]) for i in range(c - 1, -1, -2)]
    # Modulo 10 of the sum of the addition of three lists
    s = sum(a + b + d) % 10
    # If s is 0, as not s will be 1
    if not s:
        # If it indicates that the number is an American Express card
        if c == 15 and number[0:2] in ["34", "37"]:
            print("AMEX")
        # If it indicates that the number is a Visa card
        elif (c == 13 or c == 16) and number[0] == '4':
            print("VISA")
        # If it indicates that the number is a Mastercard card
        elif c == 16 and number[0:2] in ["51", "52", "53", "54", "55"]:
            print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")


if __name__ == '__main__':
    main()
