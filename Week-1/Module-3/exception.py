try:
    result = 10 / 0
    print(result)

except Exception as e:
    print(e)
finally:
    print('This will always execute')