#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Output the random number
print("Last digit of", number, "is", end=' ')

# Get the last digit of the number
last_digit = abs(number) % 10

# Determine the conditions based on the last digit
if last_digit > 5:
    print(last_digit, "and is greater than 5")
elif last_digit == 0:
    print(last_digit, "and is 0")
else:
    print(last_digit, "and is less than 6 and not 0")
