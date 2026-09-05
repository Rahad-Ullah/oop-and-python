name = 'Rahad Ullah'
city = "Dhaka"
address = """
    123 Main st
    Dhaka
    Bangladesh
"""

print(name)
print(city)
print(address)

# string is a sequence of characters
print(name[0])      # first character
print(name[-1])     # last character
print(name[::-1])   # reverse the string 

if 'Bangladesh' in address:
    print('Yes, he is from Bangladesh')

# string is immutable
# name[0] = 'r'       # error

# string methods
print(len(name))    # length
print(name.upper()) # uppercase
print(name.lower()) # lowercase
print(name.find('Ullah'))   # find index
print(name.replace('Ullah', 'Rahad'))   # replace
print(name.split(' '))  # split and return a list
print(name.startswith('R')) # check if starts with
print(name.endswith('H'))   # check if ends with