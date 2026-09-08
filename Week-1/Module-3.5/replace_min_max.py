length = int(input())
numbers = [int(x) for x in input().split()]

min_val = min(numbers)
max_val = max(numbers)

min_idx = numbers.index(min_val)
max_idx = numbers.index(max_val)

numbers[min_idx], numbers[max_idx] = numbers[max_idx], numbers[min_idx]

print(*numbers)