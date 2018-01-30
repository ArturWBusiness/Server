"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
# Try 1
# no idea
number = int(input("Number:"))
numbers = []
i = 1
while True:
    print(str(i))
    i += i
    if i > number:
        break

print("Largest factor is" + str(numbers[len(numbers)-1]))
