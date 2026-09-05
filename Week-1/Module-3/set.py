# set is collection of unique elements
# set is unordered, not indexed
# set is mutable, elements can be added or removed, but not changed

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1)
print(set2)

# set is not indexed
# print(set1[0])  # error

set1.add(6)
print(set1)

set1.remove(6)
print(set1)

# set is iterable
for i in set1:
    print(i)

if 1 in set1:
    print('Exists')
else:
    print('Not exists')

print(set1.union(set2))
print(set1 | set2)
print(set1.intersection(set2))
print(set1 & set2)
print(set1.difference(set2))
print(set1 - set2)
print(set2.difference(set1))
print(set2 - set1)