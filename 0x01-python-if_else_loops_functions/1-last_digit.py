#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last = str(number)[-1]
if number > 0:
    if int(last) > 5:
        print(f'Last digit of {number} is {last} and is greater than 5')
    elif int(last) == 0:
        print(f'Last digit of {number} is {last} and is 0')
    else:
        print(f'Last digit of {number} is {last} and is less than 6 and not 0')
else:
    if int(last) == 0:
        print(f'Last digit of {number} is {last} and is 0')
    else:
        print(f'Last digit of {number} is -{last} and is less than 6 and not 0')
