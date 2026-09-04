balance = 1000

def buy_things(item, price):
    # local variable
    # can be access global variable here but cannot assign on global variable
    # if we want to assign on global variable, we have to use global keyword
    global balance
    balance -= price
    print(f'balance after buying {item}: {balance}')

buy_things('phone', 1000)
buy_things('laptop', 2000)