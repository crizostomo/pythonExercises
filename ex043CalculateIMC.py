#O IMC é reconhecido como padrão internacional
# para avaliar o grau de sobrepeso e obesidade.
# É calculado dividindo o peso (em kg) pela
# altura ao quadrado (em metros).

from time import sleep
from math import pow

weight_in_KG = float(input('Please, inform your weight in KG'))
height_in_metres = float(input('Please, inform your height in metres'))
IMC = weight_in_KG / (height_in_metres**2)
if IMC < 18.5:
    print('You are underweight')
elif IMC >= 18.5 and IMC <= 25:
    print('Ideal Weight')
elif IMC > 25 and IMC <= 30:
    print('You are overweight')
else:
    print('morbid obesity')
