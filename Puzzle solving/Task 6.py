"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and
the square of thesum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
# Try 1
until = int(input("Number: "))
# sum of the squares
i = 1
total_of_squared = 0
while i <= until:
    total_of_squared += i * i
    i += 1
# square of the sums
squared_of_total = 0
i = 1
while i <= until:
    squared_of_total += i
    i += 1
squared_of_total *= squared_of_total

answer = squared_of_total - total_of_squared
print("Answer = " + str(answer))
