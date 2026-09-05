numbers = [1, 2, 3, 4, 5]

doubled = map(lambda x: x*2, numbers)   # map(function, iterable) -> returns a map object
print(list(doubled))                    # convert map object to list

squared = map(lambda x: x**2, numbers)
print(list(squared))