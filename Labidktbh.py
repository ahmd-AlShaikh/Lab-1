

infile=open('car.txt', 'r')
totalMiles =0
totalGallons=0
totalmilesgallons=0
count=0
for line in infile:
    carno=line.split()[0]
    Miles=line.split()[1]
    Gallons=line.split()[2]
    MilkesGallons= int(Miles)/int(Gallons)
    print(f"{carno}, {Miles}, {Gallons}, {MilkesGallons}")

