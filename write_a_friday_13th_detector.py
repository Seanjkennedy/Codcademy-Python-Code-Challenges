# 2. Write a Friday 13th detector
"""Create a function in Python that accepts two parameters. They’ll both be numbers. 
The first will be the month as a number, and the second will be the four-digit year. 
The function should parse the parameters and return True if the month contains a Friday the 13th and False if it doesn’t."""

from datetime import date

def is_friday_13th(year, month):

    day_of_month = 13
    d = date(year, month, day_of_month)
    queried_date = d.weekday()

    return True if queried_date == 4 else False

print(is_friday_13th(2021, 7), "\tShould return False")
print(is_friday_13th(2021, 8), "\tShould return True")
print(is_friday_13th(2022, 5), "\tShould return True")
print(is_friday_13th(2021, 10), "\tShould return False")
print(is_friday_13th(2021, 11), "\tShould return False")
