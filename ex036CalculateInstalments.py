houseValue = int(input('How much does it cost the house? '))
salaryValue = int(input('Please, type your salary '))
timeToPayInYears = int(input('How long are you planning to pay? '))

allowedValue = salaryValue*0.3
timeInMonths = timeToPayInYears*12
instalment = houseValue // timeInMonths

if instalment <= allowedValue:
    print('Congratulations, you are allowed to buy this house,'
          'the calculated monthly instalment is {} and 30% of your salary is {}'.format(instalment, allowedValue))
else:
    print('Unfortunately you are not allowed to buy this house')

print('------End of Report------')