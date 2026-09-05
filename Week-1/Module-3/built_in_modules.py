from math import *
from random import *
from time import *
from datetime import *

print(floor(2.9))   # round down
print(ceil(2.9))    # round up
print(round(2.9))   # round to nearest
print(sqrt(9))      # square root

print(random())     # 0.0 to 1.0
print(randint(1, 10))   # random number between 1 and 10
print(choices(['apple', 'banana', 'cherry']))   # random choice

sleep(2)    # wait for 2 seconds
print('hello world')

print(datetime.now())   # current date and time
print(datetime.today()) # current date
print(datetime(2022, 3, 4, 5, 6, 7))    # specific date and time
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)