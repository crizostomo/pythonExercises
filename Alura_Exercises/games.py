import  forca
import guess_game

def choose_game():
    print('*'*20)
    print('Choose your game!')
    print('*'*20)

    print('(1) Forca (2) Guess Game')

    game = int(input("What game? "))

    if(game == 1):
        print('Playing Forca game')
        forca.play()
    elif(game == 2):
        print('Playing Guess Game game')
        guess_game.play()

if(__name__ == "__main__"):
    choose_game()