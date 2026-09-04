print('Now I need money')
# money = input()
my_money = input("How much money do you have? ")
print('You have', my_money, 'dollars')

given_money = input("How much money do you give? ")
print('You have given', given_money, 'dollars and I have', my_money, 'dollars')
print('You have total', int(my_money) + int(given_money) , 'dollars')