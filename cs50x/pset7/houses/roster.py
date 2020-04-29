# Import the required libraries and functions
from cs50 import SQL
from sys import argv, exit


# If cmd input not given, exit with error code 1
if len(argv) != 2:
    print("Oopsie, Byeee!")
    exit(1)


# Establish connection with the database
db = SQL("sqlite:///students.db")


# Execute a search query by selecting all columns from students in house given as input
# and sorted by last name, if last name is same, sort by first name
lists = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", argv[1])


# Iterate through the list of dictionaries returned by the query where each dict is
# a student's info
for i in lists:
    # If the student has middle name
    if i['middle'] != None:
        # Print the fn, mn and ln with birth in this format
        print("{} {} {}, born {}".format(i['first'], i['middle'], i['last'], i['birth']))
    # If the student does not have middle name
    else:
        # Print the fn and ln with birth in this format
        print("{} {}, born {}".format(i['first'], i['last'], i['birth']))