number4digits = int(input('please type the number'))

unit = number4digits // 1 % 10
ten = number4digits // 10 % 10
hundred = number4digits // 100 % 10
thousand = number4digits // 1000 % 10


print('the unit is', format(unit))
print('the ten is', format(ten))
print('the hundred is', format(hundred))
print('the thousand is', format(thousand))