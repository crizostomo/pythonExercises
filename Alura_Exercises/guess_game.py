import random
from random import randint
def play():

    print('*'*20)
    print('Welcome to the guess game')
    print('*'*20)

    secret_number = random.randint(0, 100)
    guess_total = 0
    points = 1000
    # -->Usar com While round = 1

    print("What difficulty level do you want?")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Define the level: "))

    if(level == 1):
        guess_total = 20
    elif(level == 2):
        guess_total = 10
    else:
        guess_total = 5


    # -->Usar com While while(round <= guess_total):
    for round in range(1, guess_total + 1):
        print('Guess {} of {}'.format(round, guess_total))

        guess_str = input('Please type a number between 1 and 100: ')
        print('You typed {}'.format(guess_str))
        guess = int(guess_str)

        if(guess <1 or guess > 100):
            print('You should type a number between 1 and 100')
            continue

        succed  = secret_number == guess_str
        higher  = guess > secret_number
        lower   = guess < secret_number

        if(succed):
            print('You guessed right and got {} points'.format(points))
            break
        else:
            if(higher):
                print('You failed! Your guess was higher than the secret number.')
            elif(lower):
                print('You failed! Your guess was lower than the secret number.')
            lost_points = abs(secret_number - guess) #Absolute number - Avoid negative
            points = points - lost_points

    #    guess_total = guess_total - 1
    # -->Usar com While    round = round + 1

    print("Game over")

if(__name__ == "__main__"):
    play()