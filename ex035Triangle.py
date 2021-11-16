x = int(input("Please type the first number"))
y = int(input("Please type the second number"))
z = int(input("Please type the third number"))
list = [x, y, z]
list.sort()
if ((list[0]+list[1] > list[2]) and (list[2]+list[1] > list[0])):
    print("It is possible to construct a triangle")
else:
    print("It is not possible to construct a triangle")