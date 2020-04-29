# Import required libraries and functions
from cs50 import SQL
import csv
from sys import exit, argv


# If no cmd input, exit with error code 1
if len(argv) != 2:
    print("Oopsie, not again!")
    exit(1)


# Establish connection with the database
db = SQL("sqlite:///students.db")


# Open the .csv file to read it
with open(argv[1], "r") as file:
    # Make a DictReader object
    read = csv.DictReader(file)
    # Iterate through the rows of dicts in the object
    for i in read:
        # Split the value to a list under the key 'name' as
        # firstn, lastn and midn contain one space between
        namel = i["name"].split()
        # Extract the house and birth year of the current dict
        house = i["house"]
        birth = i["birth"]
        # If the student has a middle name
        if len(namel) == 3:
            firstn = namel[0]
            midn = namel[1]
            ln = namel[2]
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", firstn, midn, ln, house, birth)
        # If the student doesn't have a middle name
        else:
            firstn = namel[0]
            lastn = namel[1]
            db.execute("INSERT INTO students (first, last, house, birth) VALUES (?, ?, ?, ?)", firstn, lastn, house, birth)