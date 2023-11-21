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
    


def displaylocation(location):               #display location
    infile=open('results.txt','r')
    lines=infile.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip()
    for line in lines:
        timestamp=line.split(',')[0]
        mylocation=line.split(',')[1]
        sensorID=line.split(',')[2]
        if mylocation==location:
            print(timestamp,location,sensorID)

def add_record():          #prompts the user to enter data of a new sensor
    sensorIDintered=input('Enter data of a new sensor')




def update(sensorIDintered):        #update sensorID
    infile=open('results.txt','r')
    lines=infile.readlines()
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
        
        if sensorID==sensorIDintered:
        
            print(timestamp,location,sensorIDintered,statusAlerts,dataType,value,batteryLevel,roomSize,installationDate)
        else:
            print("error massage")    
  


def updatedatatype(datatypegiven):     #update datatype 
    
    infile=open('results.txt','r')
    
    lines=infile.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip()
    for line in lines:
        timestamp=line.split(',')[0]
        mylocation=line.split(',')[1]
        sensorID=line.split(',')[2]
        StatusAlerts=line.split(",")[3]
        datatype=line.split(',')[4]
        if datatype==datatypegiven:
            print(timestamp,mylocation,sensorID,StatusAlerts,datatypegiven)
        else:
            print("error")    
updatedatatype("Temperature")

