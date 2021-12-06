import random


def play():

    print_opening_message()
    secret_word = loading_secret_word()

#    print(words)

#    secret_word = "java".upper()
#    letters_right = ["_" for letter in secret_word]
    letters_right = initiate_letters_right(secret_word)
    print(letters_right)

#    for letter in letters_right:
#       letters_right.append("_")

    hung = False
    got_it_right = False
    errors = 0


    while(not hung and not got_it_right):

        guess = ask_guess()

        if(guess in secret_word):
            check_correct_guess(guess, letters_right, secret_word)
        else:
            errors += + 1
            hung_draw(errors)

        hung = errors == 7
        got_it_right = "_" not in letters_right #Acertou quando o '_' não estiver em letras acertadas
        print(letters_right)

    if(got_it_right):
        print("Congrats, you won!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Well, you were hung!")
        print("The word was {}".format(secret_word))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    print("Game over")



def hung_draw(errors):
    print("  _______     ")
    print(" |/      |    ")

    if (errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def check_correct_guess(guess, letters_right, secret_word):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            letters_right[index] = letter
        #                print('Found the letter {} in the position {}'.format(letter, index))
        index += + 1

def ask_guess():
    guess = input('What letter? ')
    guess = guess.strip().upper()
    return guess

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