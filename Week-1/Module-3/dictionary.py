# dictionary is a collection of key-value pairs

person = {'first_name': 'John', 'last_name': 'Smith', 'age': 20}

print(person)
print(person.get('first_name'))
print(person['last_name'])

# dictionary is iterable
for key in person:
    print(key, ':', person[key])

for key, value in person.items():
    print(key, '->', value)

# dictionary is mutable
person['first_name'] = 'Rahad'
print(person)

# dictionary is not indexed or ordered
# print(person[0])    # error

# dictionary methods
print(person.keys())    # return keys as list
print(person.values())  # return values as list
print(person.items())   # return items as list of tuples

person['city'] = 'Dhaka'    # add or update key-value
person.update(district = 'Sylhet')  # add or update key-value
print(person)

person.pop('city')  # remove key-value
print(person)

person.clear()  # clear the dictionary
print(person)