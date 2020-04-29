# Import required libraries
import csv
from sys import exit, argv


# If cmd args are less than 3, exit with error code 1
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)


# Open the text file and read the dna sequence to abc variable
with open(argv[2], "r") as file1:
    abc = file1.readline()

# Open the csv file as a dictreader object
i = csv.DictReader(open(argv[1], "r"))


# A list of dictionaries iterating over keys and values in an object
# iterating over the dictreader object
dict3 = [{k: v for k, v in m.items()} for m in i]


# The columns pfft... to know which dna strands to check for
cols = [a for a in dict3[0].keys()]


# Total number of strands to check
totaldna = len(cols) - 1


dict2 = {}


# Iterating over the column names
for i in cols:
    # If column is not a dna strand
    if i == 'name':
        continue
    # Set a variable to the strand
    str1 = i
    # 2 count vars because a strand can occur more than once
    count = 0
    count1 = 0
    # To iterate over string
    current = 0
    # To check if this is the first strand encountered
    flag = 0
    # While the variable is less than string length
    while current != len(abc):
        # If this is the first occurence of the strand in sequence
        if flag == 0:
            # While there are 2 strands next to each other and length is less than total length
            while abc[current:current+len(str1)] == str1 and abc[current + len(str1):current + (len(str1) * 2)] == str1 and current < len(abc):
                # Increase count and increase the current var by strand len
                # Because we already checked the other parts in between
                count1 += 1
                current += len(str1)
                # Set flag to 1 because the first occurence is over
                flag = 1
        # If this is not the first occurence
        else:
            # Again count the number of strands
            while abc[current:current+len(str1)] == str1 and abc[current + len(str1):current + (len(str1) * 2)] == str1 and current < len(abc):
                # Increase count and current var
                count += 1
                current += len(str1)
            # If the first occuring std count is less than this one,
            # Change it to this one, because we have to check for
            # Longest std's of a strand :)
            if count > count1:
                count1 = count
        # If it is not the start of a std, just increment by 1
        current += 1
    # For each strand, set the strand as key and the count1 obtained as value in dict
    # We have to increment count1 because we checked for strands next to each other
    # And the last part of an std would not pass the condition because the part next to it
    # will not be itself
    dict2[str1] = count1 + 1


# Iterate through the list of dictionaries
for i in dict3:
    # Set count to 0
    # Count is variable indicating how many strands are identical
    count = 0
    # For each key, value pair in dicts
    for j, k in i.items():
        # If key is name, skip
        if j == 'name':
            continue
        else:
            # If the same strand value in dict2 is equal to its value in i
            if dict2[j] == int(k):
                # Increment the count indicating that one strand is equal
                count += 1
            # If only some strands are equal, and any strand that is not equal
            # is obtained, break from loop, because all std counts should be equal
            else:
                break
    # If count, indicating total equal std counts, is equal to the total strand count
    # meaning that all std counts of strands match
    if count == totaldna:
        # Print the value from the key 'name' of that dictionary
        print(i['name'])
        # Exit with exit code 0
        exit(0)
# If program is still running, meaning there is no match,
# print no match
print("No match")
