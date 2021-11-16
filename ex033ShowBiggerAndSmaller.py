num1 = int(input("Please type the first number"))
num2 = int(input("Please type the second number"))
num3 = int(input("Please type the third number"))

#One Way to do this exercise
#cond1 = num1 > num2
#cond2 = num1 > num3
#cond3 = num2 > num1
#cond4 = num2 > num3
#cond5 = num3 > num1
#cond6 = num3 > num2
#
#
#print("Num1 Is the Highest" if cond1 and cond2 == True else "")
#print("Num2 Is the Highest" if cond3 and cond4 == True else "")
#print("Num3 Is the Highest" if cond5 and cond6 == True else "")
#print("Num1 Is the Smallest" if (cond1 and cond2) == False else "")
#print("Num2 Is the Smallest" if (cond3 or cond4) == False else "")
#print("Num3 Is the Smallest" if (cond5 or cond6) == False else "")

#A second way to do this exercise

list = [num1, num2, num3]
list.sort()
print("The smallest number is", list[0], "and the highest number is", list[2])



