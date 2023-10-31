#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
line = "Last digit of "
if number > 0:
    ld = number % 10
else:
    ld = number % -10
if ld > 5:
    print("{}{:d} is {:d} and is greater than 5".format(line, number, ld))
elif ld == 0:
    print("{}{:d} is {:d} and is 0".format(line, number, ld))
else:
    print("{}{:d} is {:d} and is less than 6 and not 0".format(line, number, ld))
