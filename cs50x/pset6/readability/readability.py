from cs50 import get_string


def main():
    # Prompt user for string
    string = get_string("Text: ")
    # Calculate words
    w = words(string)
    # Calculate sentences
    s = sentences(string)
    # Calculate letters
    l = letters(string)
    # Average
    L = (100 * l) / w
    S = (100 * s) / w
    # Calculate grade
    grade = round((0.0588 * L) - (0.296 * S) - 15.8)
    # If grade is higher than or equal to 16
    if grade >= 16:
        print("Grade 16+")
    # If grade is lower than 1
    elif grade < 1:
        print("Before Grade 1")
    # If grade is between 1 and 15
    else:
        print("Grade " + str(grade))


# Function to calculate words
def words(string: str) -> int:
    # Spaces indicate start of word, assuming that only one space exists between each word
    return string.count(" ") + 1


# Function to calculate sentences
def sentences(string: str) -> int:
    # Set count to 0
    count = 0
    # Loop through the length of string
    for i in range(len(string)):
        # If the current char is any of the punctuation marks and the character preceding it is alphanumeric
        if (string[i] == '?' or string[i] == '.' or string[i] == '!') and string[i-1].isalnum() == True:
            # Append count
            count += 1
    # Return count
    return count


# Function to calculate letters
def letters(string: str) -> int:
    # Return the sum of list
    return sum(i.isalpha() for i in string)


# Actually an important step since you can't use functions before defining them
# but this way you can avoid it
if __name__ == '__main__':
    main()