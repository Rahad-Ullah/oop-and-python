length = int(input())
numbers = [int(x) for x in input().split()]

operations = 0
oddFound = False

while(oddFound == False):
    for i in range(length):
        if(numbers[i] % 2 == 0):
            numbers[i] = numbers[i] / 2
        else:
            oddFound = True
            break

    if(oddFound == False):
        operations += 1
        
print(operations)