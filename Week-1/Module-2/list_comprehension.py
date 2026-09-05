numbers = [45, 67, 89, 12, 34, 56, 78, 90, 11, 33, 55, 77, 99]
odds = []
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
print(odds)

# list comprehension (not readable)
odds = [num for num in numbers if num % 2 == 1 and num % 5 == 0]
print(odds)


