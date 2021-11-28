import random

num0 = str('pedra')
num1 = str('papel')
num2 = str('tesoura')
list = [num0, num1, num2]
#A list is in []
randomCompDraw = random.choice(list)
yourChoice = str(input("Please choose, pedra, papel ou tesoura ".upper()))

if randomCompDraw == 'pedra' and yourChoice == 'tesoura':
    print('The computer won, because it chose pedra and you chose tesoura')
elif randomCompDraw == 'papel' and yourChoice == 'pedra':
    print('The computer won, because it chose papel and you chose pedra')
elif randomCompDraw == 'tesoura' and yourChoice == 'papel':
    print('The computer won, because it chose tesoura and you chose papel')
elif yourChoice == 'pedra' and randomCompDraw == 'tesoura':
    print('You won, because you chose pedra and the computer chose tesoura')
elif yourChoice == 'papel' and randomCompDraw == 'pedra':
    print('You won, because you chose papel and the computer chose pedra')
elif yourChoice == 'tesoura' and randomCompDraw == 'papel':
    print('You won, because you chose tesoura and the computer chose papel')
elif yourChoice == 'pedra' and randomCompDraw == 'pedra':
    print('Nobody won, because you chose pedra and the computer chose pedra')
elif yourChoice == 'papel' and randomCompDraw == 'papel':
    print('Nobody won, because you chose papel and the computer chose papel')
else:
    print('Nobody won, because you chose tesoura and the computer chose tesoura')
print('The computer chose', randomCompDraw)