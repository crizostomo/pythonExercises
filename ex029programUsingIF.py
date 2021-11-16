speedLimit = int(input("Please type the speed "))
print("Speed ok" if speedLimit <=80 else ("You've just got a fine of R$", (speedLimit-80)*7))
