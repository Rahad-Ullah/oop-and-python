# index =  0  1  2  3  4  5  6  7  8  9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index = -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(numbers[3])
print(numbers[-3])

# list slicing: list([start:end:step])
print(numbers[3:7:1])
print(numbers[3:])
print(numbers[:7])
print(numbers[:])

# reverse list
print(numbers[::-1])