KMPrice = float(input("What is the distance in KM? "))
if KMPrice <= 200.0:
    print("The price is {}".format(KMPrice*0.5))
else:
    print("The price is {}".format(KMPrice*0.45+10))
