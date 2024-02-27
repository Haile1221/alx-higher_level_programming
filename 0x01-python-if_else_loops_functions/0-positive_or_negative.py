#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Output the random number
print(number, end=' ')

# Determine if the number is positive, negative, or zero
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
