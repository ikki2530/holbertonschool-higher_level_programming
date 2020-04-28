#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = "Last digit of " + str(number) + " is "
if number >= 0:
    dig = number % 10
    if dig > 5:
        st = st + str(dig) + " and is greater than 5"
    elif dig == 0:
        st = st + str(dig) + " and is 0"
    else:
        st = st + str(dig) + " and is less than 6 and not 0"
else:
    number = number * (-1)
    dig = number % 10
    dig = (-1) * dig
    if dig == 0:
        st = st + str(dig) + " and is 0"
    else:
        st = st + str(dig) + " and is less than 6 and not 0"
print(st)
