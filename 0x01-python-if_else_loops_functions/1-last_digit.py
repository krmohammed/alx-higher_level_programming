#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number > 0:
    last = number % 10
else:
    last = -((-number) % 10)

print("Last digit of {:d} is {:d}".format(number, last), end=' ')
if last > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
