def full_name(first, last):
    return f'{first} {last}'

print(full_name(first='John', last='Smith'))    # serial arguments
print(full_name(last='Smith', first='John'))    # non serial arguments

def full_name(first, last, *args):  # args is a tuple
    return f'{first} {last} {args}'

print(full_name('John', 'Smith', 'Dhaka', 'Bangladesh'))

def full_name(first, last, **kwargs):    # kwargs is a dictionary
    return f'{first} {last} {kwargs['district']} {kwargs["country"]}'

print(full_name('John', 'Smith', district='Dhaka', country='Bangladesh'))