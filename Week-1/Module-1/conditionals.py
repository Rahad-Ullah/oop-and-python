# in, not, not in, and, or, is, is not

a = 10
b = 3

if a > b:
    print('a is greater than b')
elif a < b:
    print('a is less than b')
else:
    print('a is equal to b')

is_alive = True
is_married = False
nationality = 'bangladeshi'

# logical and, or, not
if is_alive and is_married:
    print('You are alive and married')
elif is_alive and not is_married:
    print('You are alive but not married')
elif not is_alive and is_married:
    print('You are not alive but married')
elif is_alive or is_married:
    print('You are alive or married')
else:
    print('You are not alive and not married')

# is, is not
if nationality is 'bangladeshi':
    print('You are Bangladeshi')
elif nationality is not 'bangladeshi':
    print('You are not Bangladeshi')
else:
    print('You are not Bangladeshi')

# in, not in
if 'bangladeshi' in nationality:
    print('You are Bangladeshi')
elif 'bangladeshi' not in nationality:
    print('You are not Bangladeshi')
else:
    print('You are not Bangladeshi')