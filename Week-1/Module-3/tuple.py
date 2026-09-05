# tuple is a sequence of immutable objects

person1 = ('John', 'Smith', 20)
person2 = 'Rahad', 'Ullah', 20

print(person1)
print(person2)

# tuple is immutable
# person1[0] = 'Rahad'

# tuple methods
print(len(person1))     # length
print(person1.count(20))    # count specific value
print(person1.index(20))    # index of specific value

# tuple unpacking
first_name, last_name, age = person1

print(first_name)
print(last_name)
print(age)

# tuple of tuples
person1 = ('John', 'Smith', 20)
person2 = ('Rahad', 'Ullah', 20)

people = (person1, person2)

print(people)

# tuple of lists
person1 = ['John', 'Smith', 20]
person2 = ['Rahad', 'Ullah', 20]

people = (person1, person2)

print(people)