import random



def play():

    print_opening_message()
    secret_word = loading_secret_word()


#    print(words)

#    secret_word = "java".upper()
#    letters_right = ["_" for letter in secret_word]
    letters_right = initiate_letters_right(secret_word)


#    for letter in letters_right:
#       letters_right.append("_")

    print(letters_right)

    hung = False
    got_it_right = False
    errors = 0


    while(not hung and not got_it_right):

        guess = input('What letter? ')
        guess = guess.strip().upper()

        if(guess in secret_word):
            index = 0
            for letter in secret_word:
                if(guess == letter):
                    letters_right[index] = letter
    #                print('Found the letter {} in the position {}'.format(letter, index))
                index += + 1
        else:
            errors += + 1

        hung = errors == 6
        got_it_right = "_" not in letters_right #Acertou quando o '_' não estiver em letras acertadas
        print(letters_right)

    if(got_it_right):
        print('You won!!')
    else:
        print('You lost!!')
    print("Game over")




def initiate_letters_right(word):
    return ["_" for letter in word]

def print_opening_message():
    print('*'*20)
    print('Welcome to the forca game')
    print('*'*20)

def loading_secret_word():
    file = open("files.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word

if(__name__ == "__main__"):
    play()