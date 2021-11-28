grade1 = float(input('Please type your first grade: '))
grade2 = float(input('Please type your first grade: '))
average = (grade1+grade2)/2
if(average < 5.0):
    print('You are out')
elif(average >= 7.0):
    print('You are in')
else:
    print('You need to study during summer')
