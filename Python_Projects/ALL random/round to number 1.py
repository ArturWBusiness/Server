
def power(number, pow):
    x = 1
    res = number
    while x < pow:
        res = res * number
        x += 1
    return res


x = 1
sum = 0 
while x < 5000:
    n = 1 / power(2, x)
    sum += n
    x += 1
print(str(sum))