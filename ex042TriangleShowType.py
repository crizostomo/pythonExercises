from time import sleep
x = float(input("Please type the first number: "))
y = float(input("Please type the second number: "))
z = float(input("Please type the third number: "))
print("PROCESSING...")
sleep(2)
list = [x, y, z]
list.sort()

if ((list[0]+list[1] > list[2]) and (list[2]+list[1] > list[0]) and (list[0]==list[1] or list[0]==list[2] or list[1]==list[2])):
    print(('It is possible to construct a triangle, this is an isosceles Triangle'))
elif ((list[0]+list[1] > list[2]) and (list[2]+list[1] > list[0]) and (list[0]==list[1]==list[2])):
    print(('It is possible to construct a triangle, this is an Equiangular Triangle'))
elif ((list[0]+list[1] > list[2]) and (list[2]+list[1] > list[0]) and (list[0]!=list[1]!=list[2])):
    print(('It is possible to construct a triangle, this is an Scalene Triangle'))
else:
    print("It is not possible to construct a triangle")
