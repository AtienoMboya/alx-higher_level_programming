#!/usr/bin/python3
import random
number = random.randint(-10000,1000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print(f"Last digit of {number} is {digit} and is ")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6and not 0")
