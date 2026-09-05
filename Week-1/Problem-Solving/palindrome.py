s = input().strip()
rev = int(s[::-1])

print(rev)
if str(rev) == s:
    print("YES")
else:
    print("NO")