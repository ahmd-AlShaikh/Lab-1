# infile = open('results.txt', 'r')
# lines = infile.readlines()
# infile.close()

# for i in range(len(lines)):
#     lines[i]=lines[i].strip()


# for line in lines:
#     timestamp=line.split(",")[0]
#     location=line.split(",")[1]
#     sensorID=line.split(",")[2]
#     statusAlerts=line.split(",")[3]
#     dataType=line.split(",")[4]
#     value=line.split(",")[5]
#     batteryLevel=line.split(",")[6]
#     roomSize=line.split(",")[7]
#     installationDate=line.split(",")[8]
    

# #[7] Display readings in a given location
# def displaylocation(location):               
#     infile=open('results.txt','r')
#     lines=infile.readlines()
#     for i in range(len(lines)):
#         lines[i]=lines[i].strip()
#     for line in lines:
#         timestamp=line.split(',')[0]
#         mylocation=line.split(',')[1]
#         sensorID=line.split(',')[2]
#         if mylocation==location:
#             print(timestamp,location,sensorID)

# def add_record():          #prompts the user to enter data of a new sensor
#     sensorIDintered=input('Enter data of a new sensor')

def main():
    x=input("location: ")
    location(x)

#[8] Display readings by a given Sensor ID
def sensorID(sensorIDintered):        
    infile=open('results.txt','r') 
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
        installationDate=installationDate.rstrip("\\")
        if timestamp=='Timestamp':

            print(f"{timestamp:19}|{location:8}|{sensorID:8}|{statusAlerts:6}|{dataType:11}|{value:13}|{batteryLevel:8}|{roomSize:13}|{installationDate:8}")
            print(" ------------------------------------------------------------------------------------------------------------ ")
        
        elif sensorID==sensorIDintered:
        
            print(f"{timestamp:19}|{location:8}|{sensorIDintered:9}|{statusAlerts:13}|{dataType:11}|{value:13}|{batteryLevel:13}|{roomSize:8}|{installationDate:8}")
        

#[6] Display readings by a given data type

def data(datatypeintered):       
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
        installationDate=installationDate.rstrip("\\")
        if timestamp=='Timestamp':

            print(f"{timestamp:19}|{location:8}|{sensorID:8}|{statusAlerts:6}|{dataType:11}|{value:13}|{batteryLevel:8}|{roomSize:13}|{installationDate:8}")
            print(" ------------------------------------------------------------------------------------------------------------ ")
        
        elif dataType==datatypeintered:
        
            print(f"{timestamp:19}|{location:8}|{datatypeintered:9}|{statusAlerts:13}|{dataType:11}|{value:13}|{batteryLevel:13}|{roomSize:8}|{installationDate:8}")



#[7] Display readings in a given location
def location(locationintered):        
    infile=open('results.txt','r') 
                
    if locationintered == 'kitchen':
        locationintered = 'Kitchen'
    elif locationintered == 'living room':
        locationintered = 'Living Room'
    elif locationintered == 'bedroom':
        locationintered = 'Bedroom'
    elif locationintered == 'office':
        locationintered = 'Office'
    elif locationintered == 'front yard':
        locationintered = 'Front Yard'
    elif locationintered == 'bathroom':
        locationintered = 'Bathroom'
    elif locationintered == 'garage':
        locationintered = 'Garage'
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
        installationDate=installationDate.rstrip("\\")
        if timestamp=='Timestamp':

            print(f"{timestamp:19}|{location:8}|{sensorID:8}|{statusAlerts:6}|{dataType:11}|{value:13}|{batteryLevel:8}|{roomSize:13}|{installationDate:8}")
            print(" ------------------------------------------------------------------------------------------------------------ ")
        
        elif location==locationintered:
        
            print(f"{timestamp:19}|{location:8}|{locationintered:9}|{statusAlerts:13}|{dataType:11}|{value:13}|{batteryLevel:13}|{roomSize:8}|{installationDate:8}")



#[9] Display details about all sensors with low level Battery"
def Battery():        
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
        batteryLevel=batteryLevel.rstrip("%")

        
        roomSize=line.split(",")[7]
        installationDate=line.split(",")[8]
        installationDate=installationDate.rstrip("\\")
        if timestamp=='Timestamp':

            print(f"{timestamp:19}|{location:8}|{sensorID:8}|{statusAlerts:6}|{dataType:11}|{value:13}|{batteryLevel:8}|{roomSize:13}|{installationDate:8}")
            print(" ------------------------------------------------------------------------------------------------------------ ")
        
        elif int(batteryLevel)<=60:
            batteryLevel=line.split(",")[6]
            print(f"{timestamp:19}|{location:8}|{sensorID:9}|{statusAlerts:13}|{dataType:11}|{value:13}|{batteryLevel:13}|{roomSize:8}|{installationDate:8}")


#[4] Display all readings"
def allreadings():       
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
        installationDate=installationDate.rstrip("\\")
        if timestamp=='Timestamp':

            print(f"{timestamp:19}|{location:11}|{sensorID:8}|{statusAlerts:13}|{dataType:15}|{value:18}|{batteryLevel:13}|{roomSize:13}|{installationDate:8}")
            print(" ------------------------------------------------------------------------------------------------------------------------------------- ")
        else:
            print(f"{timestamp:19}|{location:11}|{sensorID:9}|{statusAlerts:13}|{dataType:15}|{value:18}|{batteryLevel:13}|{roomSize:13}|{installationDate:8}")

            
         

allreadings()
