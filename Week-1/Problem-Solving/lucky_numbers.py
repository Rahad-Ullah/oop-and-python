a, b = map(int, input().split())

found = False

for i in range(a, b + 1):
    chars = str(i)
    for char in chars:
        if char != '4' and char != '7':
            break
    else:
        print(i, end=' ')
        found = True

if not found:
    print(-1)