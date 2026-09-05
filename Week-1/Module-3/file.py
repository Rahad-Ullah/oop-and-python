# .csv comma separated value
# .txt tab separated value
# .json javascript object notation

# write file
with open('file.txt', 'w') as file:
    content = file.write('Hello world!')
    print(content)

# read file
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)