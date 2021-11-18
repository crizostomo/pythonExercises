from random import randint
from time import sleep
computer = randint(0, 5)
player = int(input("In what number did I think?"))
print('-=-'*20)
print("PROCESSING...")
sleep(2)
if player == computer:
    print("Congratulations you beat me")
else:
    print("I won! I thought in the number {} and not in the number {}".format(computer, player))