from time import sleep
num1 = int(input("Please type the first number: "))
num2 = int(input("Please type the second number: "))

list = [num1, num2]
list.sort()
if(list[0] > list[1]):
    print("PROCESSING...")
    sleep(2)
    print('The number {} is higher than number {}'.format(list[0], list[1]))
elif(list[0] < list[1]):
    print("PROCESSING...")
    sleep(2)
    print('The number {} is lower than number {}'.format(list[0], list[1]))
else:
    print("PROCESSING...")
    sleep(2)
    print('The number {} is equal to the number {}'.format(list[0], list[1]))

print('-=-'*20)

