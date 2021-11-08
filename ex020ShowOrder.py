import random
name1 = input('please type the name 1: ')
name2 = input('please type the name 2: ')
name3 = input('please type the name 3: ')
name4 = input('please type the name 4: ')
list = [name1, name2, name3, name4]
#A list is in []
randomDraw = random.choice(list)
print('the selected name was {}'.format(randomDraw))
