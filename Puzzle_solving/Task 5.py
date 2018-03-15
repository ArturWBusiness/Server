"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# Attempt 1 (redo, take 2min to find it...)
max_number = int(input("Smallest multiple of: "))
i = 1
while True:
    correct = True
    for x, temp in enumerate([""]*max_number):
        number = x + 1
        if i % number == 0:
            pass
        else:
            correct = False
            break
    if correct:
        print("Smallest multiple of " + str(max_number) + " is " + str(i))
        break
    if i % 1000000 == 0:
        print(str(i))
    i += 1
