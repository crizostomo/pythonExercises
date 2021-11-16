import random

num0 = 0
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
list = [num0, num1, num2, num3, num4, num5]
#A list is in []
randomCompDraw = random.choice(list)
yourNum = int(input("Please type one number from 0 to 5 "))
print(yourNum == randomCompDraw)
print("the computher thought in the number", randomCompDraw)
