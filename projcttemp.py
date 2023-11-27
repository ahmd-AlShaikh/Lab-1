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
    sensorIDintered=input("Enter the new sensorID")             #Done
    sensorIDintered=sensorIDintered.upper()
    lines=infile.readlines()
    
                        #انا مش عارف ليه بيعمل الwhile بعديو بيوقف
    
  
   
             
        
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
        if timestamp=='Timestamp' and location=="Location" and sensorID=="Sensor ID" and statusAlerts=="Status/Alerts" and dataType=="Data Type" and value=="Value" and  batteryLevel=="Battery Level" and roomSize=="Room Size" and installationDate=="Installation Date":

            print(f"{timestamp:20}|{location:15}|{sensorID:13}|{statusAlerts:15}|{dataType:15}|{value:30}|{batteryLevel:18}|{roomSize:12}|{installationDate:25}")
        
        elif sensorID==sensorIDintered:
        
            print(f"{timestamp},{location},{sensorIDintered},{statusAlerts},{dataType}{value}{batteryLevel}{roomSize}{installationDate}")
        


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
            print(f"{timestamp},{mylocation},{sensorID},{StatusAlerts},{datatypegiven}")
        else:
            print("error")    





update('S11')

