import math
from math import pow, sqrt, hypot
OpCat = float(input('please type the opposite cateto'))
AdjCat = float(input('please type the adjacent cateto'))
aPow = pow(OpCat, 2)
bPow = pow(AdjCat, 2)
Hypotenuse = sqrt(aPow+bPow)
HypotenuseMethod2 = math.hypot(OpCat, AdjCat)
print('the hypotenuse of {} and {} is {}'.format(OpCat, AdjCat, Hypotenuse))
print('the hypotenuse of {} and {} is {}'.format(OpCat, AdjCat, HypotenuseMethod2))