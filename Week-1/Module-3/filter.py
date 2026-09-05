actors = [
    {'name': 'John', 'age': 30, 'gender': 'male'},
    { 'name': 'Jane', 'age': 25, 'gender': 'female'},
    { 'name': 'Bob', 'age': 35, 'gender': 'male'},
    { 'name': 'Alice', 'age': 28, 'gender': 'female'}
]

juniors = filter(lambda actor: actor['age'] < 30, actors)   # filter(function, iterable) -> returns a filter object
print(list(juniors))