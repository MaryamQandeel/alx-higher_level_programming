#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    ld = number % 10
else:
    ld = number % -10
    line = "Last digit of {:d} is {:d} and is"
if ld > 5:
    print("{} greater than 5".format(line,number, ld))
elif ld == 0:
    print("{} 0".format(line, number, ld))
else:
    print("{} less than 6 and not 0".format(line, number, ld))
