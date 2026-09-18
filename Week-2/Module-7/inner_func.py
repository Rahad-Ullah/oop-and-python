# function is a first class object in python
# function can be assigned to a variable
# function can be passed as an argument to another function
# function can be returned from another function
# function can be nested

def double_decker():
    print('Starting double decker')
    def inner_func():
        print('Starting inner function')
        return 'hello world'
    return inner_func

# print(double_decker()())

def do_something(work):
    print('Starting do something')
    work()

do_something(double_decker())