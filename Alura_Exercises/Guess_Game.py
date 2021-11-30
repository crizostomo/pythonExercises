print('*'*20)
print('Welcome to the guess game')
print('*'*20)

secret_number = 42

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

print("Game over")