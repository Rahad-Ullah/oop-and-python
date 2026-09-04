numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers.append(11)  # add at the end (push)
print(numbers)

numbers.insert(0, 0) # add at specific index
print(numbers)

numbers.remove(0)   # remove specific value
print(numbers)

last_value = numbers.pop()   # remove last value and return it
print(last_value)

numbers.clear()     # clear the list
print(numbers)

index = numbers.index(5)    # return index of specific value
print(index)

count = numbers.count(5)    # return count of specific value
print(count)

sorted = numbers.sort()      # sort the list
print(sorted)

reversed = numbers.reverse()   # reverse the list
print(reversed)

replica = numbers.copy()      # copy the list
print(replica)