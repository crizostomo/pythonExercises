width = int(input('please type the width in metres'))
height = int(input('please type the height in metres'))
squareMetre = width*height
paintEfficiency = 2
amountOfPaintNeeded = squareMetre/paintEfficiency
print('Widht = {},\nHeight {},\n,this is equals to {}m² and it is needed {} litres of paint'.format(width, height, squareMetre, amountOfPaintNeeded))