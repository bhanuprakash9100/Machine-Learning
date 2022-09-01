y = []
for i in range(4):
    x=int(input("Enter the weight:"))
    y.append(x)
    print("Lbs list:", y)
    kilograms = []
    for w in y:
        kgs=(w/2.205)
        kilograms.append(kgs)
        print("KGs list:", kilograms)



