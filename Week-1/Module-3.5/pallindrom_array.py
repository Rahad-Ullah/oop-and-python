n = int(input())
arr = list(map(int, input().split()))
reversedArr = arr[::-1]

if arr == reversedArr:
    print("YES")
else:
    print("NO")