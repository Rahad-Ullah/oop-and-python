def sum(num1, num2, num3=0):
    return num1 + num2 + num3

print(sum(5, 7))
print(sum(5, 7, 9))


def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum(5, 7))
print(sum(5, 7, 9))
print(sum(5, 7, 9, 11, 13, 15, 17, 19))