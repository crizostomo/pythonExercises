amountOfKM = int(input('How many kilometres that you used?'))
amountOfDays = int(input('How many days that you used?'))
priceToPay = (amountOfDays*60)+(amountOfKM*0.15)
print('Since you spent {} days with the car and you travelled {} kilometres, you need to pay R${}'.format(amountOfDays, amountOfKM, priceToPay))
