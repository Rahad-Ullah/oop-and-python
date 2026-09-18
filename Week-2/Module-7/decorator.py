def timer(func):
    def inner():
        print('Starting timer')
        func()
        print('Ending timer')
    return inner

@timer                     # decorator -> takes get_factorial() as an argument and returns inner
def get_factorial():
    print('Starting get_factorial')

# timer(get_factorial)()    # without decorator -> calling get_factorial()

get_factorial()             # with decorator -> calling get_factorial()