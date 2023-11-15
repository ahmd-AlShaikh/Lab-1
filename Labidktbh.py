

# infile=open('car.txt', 'r')
# totalMiles =0
# totalGallons=0
# totalmilesgallons=0
# count=0
# for line in infile:
#     carno=line.split()[0]
#     Miles=line.split()[1]
#     Gallons=line.split()[2]
#     MilkesGallons= int(Miles)/int(Gallons)
#     print(f"{carno}, {Miles}, {Gallons}, {MilkesGallons}")

infile = open('results.txt', 'r')
lines = infile.readlines()
infile.close()

for i in range(len(lines)):
    lines[i]=lines[i].strip()


for line in lines:
    timestamp=line.split(",")[0]
    location=line.split(",")[1]
    sensorID=line.split(",")[2]
    statusAlerts=line.split(",")[3]
    dataType=line.split(",")[4]
    value=line.split(",")[5]
    batteryLevel=line.split(",")[6]
    roomSize=line.split(",")[7]
    installationDate=line.split(",")[8]
    



def displaylocation(location):
    infile=open('results.txt','r')
    lines=infile.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip()
    for line in lines:
        timestamp=line.split(",")[0]
        mylocation=line.split(',')[1]
        sensorID=line.split(',')[2]
        if mylocation==location:
            print(timestamp,location,sensorID)





displaylocation("Kitchen")






newfilelist=[]

for i in range(len(lines)):
    lines[i]=lines[i].strip()
for line in lines:
    timestamp=line.split(",")[0]
    mylocation=line.split(',')[1]
    sensorID=line.split(',')[2]
    if mylocation!='Kitchen':
        newfilelist.append(line)
    

outfile=open('results.txt', 'w')
for line in newfilelist:
    outfile.write(line+'\n')
outfile.close