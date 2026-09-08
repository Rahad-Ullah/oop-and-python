str = input()
result = []
current = ""
balance = 0

for char in str:
    current += char
    if char == 'L':
        balance += 1
    else:
        balance -= 1

    if balance == 0:
        result.append(current)
        current = ""

print(len(result))

for item in result:
    print(item)