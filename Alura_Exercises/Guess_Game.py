print('*'*20)
print('Welcome to the guess game')
print('*'*20)

secret_number = 42
guess_total = 3
# -->Usar com While round = 1

# -->Usar com While while(round <= guess_total):
for round in range(1, guess_total + 1):
    print('Guess {} of {}'.format(round, guess_total))
    guess_str = input('Please type your number: ')
    print('You typed {}'.format(guess_str))
    guess   = int(guess_str)

    succed  = secret_number == guess_str
    higher  = guess > secret_number
    lower   = guess < secret_number

    if(succed):
        print('You guessed right')
    else:
        if(higher):
            print('You failed! Your guess was higher than the secret number.')
        elif(lower):
            print('You failed! Your guess was lower than the secret number.')

#    guess_total = guess_total - 1
# -->Usar com While    round = round + 1

print("Game over")