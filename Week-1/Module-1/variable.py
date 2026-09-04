age = 23
interest_rate = 3.5
name = 'John Smith'
district = "Dhaka"
is_alive = True
is_married = False

print(age)
print(interest_rate)
print(name)
print(district)
print(is_alive)
print(is_married)

print(type(age))
print(type(interest_rate))
print(type(name))
print(type(district))
print(type(is_alive))
print(type(is_married))

# output
""" 
    <class 'int'>
    <class 'float'>
    <class 'str'>
    <class 'str'>
    <class 'bool'>
    <class 'bool'>
"""

print('My name is ' + name + ' and I am ' + str(age) + ' years old')
print(f'My name is {name} and I am {age} years old')