"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# Try 1
max_len = int(input("Length of products to make the palindrome:\n> "))
value1 = 1
value2 = 1
value3 = 1
answer_value = 0


def palindermic(number):
    number = str(number)
    i = 0  # item
    while True:
        last = len(number) - 1 - i
        if i == last or last < i:
            return True
        if number[i] == number[last]:
            pass
        else:
            return False
        i += 1


while True:
    if len(str(value1)) > max_len:
        value1 = 1
        value2 += 1
    if len(str(value2)) > max_len:
        break
    value3 = value1*value2

    if palindermic(value1*value2) and answer_value < value3:
        answer_value = value3
        print("Found: " + str(value1) + " * " + str(value2) + " = " + str(value3))
        answer = str(value1) + " * " + str(value2) + " = " + str(value3)

    value1 += 1

print(answer)