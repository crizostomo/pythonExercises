RaiseInSalary = float(input("Please type your salary"))
if RaiseInSalary >= 1250.0:
    print("Your raise is {}".format(RaiseInSalary*0.1))
else:
    print("Your raise is {}".format(RaiseInSalary*0.15-62.5))