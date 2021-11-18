from datetime import date
LeapYear = int(input("Please type the year "))
if LeapYear ==0:
        LeapYear = date.today().year
#print("This is a leap year" if LeapYear % 4 == 0 else "This is not a leap year")
print("This is a leap year" if LeapYear % 4 == 0 and LeapYear % 100 !=0 or LeapYear % 400 == 0 else "This is not a leap year")