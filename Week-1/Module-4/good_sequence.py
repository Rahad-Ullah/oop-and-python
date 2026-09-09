import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit(0)

n = int(input_data[0])
numbers = [int(x) for x in input_data[1:n + 1]]

freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1

remove_count = 0
for num, count in freq.items():
    if count >= num:
        remove_count += (count - num)
    else:
        remove_count += count

print(remove_count)