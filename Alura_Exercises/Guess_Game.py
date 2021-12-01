import random
from random import randint

print('*'*20)
print('Welcome to the guess game')
print('*'*20)

secret_number = random.randint(0, 100)
guess_total = 3
# -->Usar com While round = 1

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
        print('You guessed right')
        break
    else:
        if(higher):
            print('You failed! Your guess was higher than the secret number.')
        elif(lower):
            print('You failed! Your guess was lower than the secret number.')

#    guess_total = guess_total - 1
# -->Usar com While    round = round + 1

print("Game over")