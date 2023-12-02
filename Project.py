###################################
# IMPORTS

import os # for temp files and for "UPDATE/DELETE reading functions"
import re # Stripping but more advanced
re.sub
###################################
# Sources
# https://www.trainingint.com/how-to-find-duplicates-in-a-python-list.html
# https://docs.python.org/3/library/stdtypes.html#str.casefold
# https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
# https://stackoverflow.com/questions/6323296/python-remove-anything-that-is-not-a-letter-or-number
# https://sebhastian.com/python-strip-multiple-characters/


###################################

def main(): # This is the main interfere for everything else
    print(list_Of_Locations)
    print(list_Of_Sensors)
    print(list_Of_DataTypes)
    print("\t\tSHM Application")
    print("\t\t   [1] Add a reading")
    print("\t\t   [2] Update a reading")
    print("\t\t   [3] Delete a reading")
    print("\t\t   [4] Display all readings")
    print("\t\t   [5] Display all readings by Status/Alerts")
    print("\t\t   [6] Display readings by a given data type")
    print("\t\t   [7] Display readings in a given location")
    print("\t\t   [8] Display readings by a given Sensor ID")
    print("\t\t   [9] Display details about all sensors with low level Battery")
    print("\t\t   [0] Exit")
    try: # This is to catch Value Errors from invalid input statements, if caught, restarts.
        redirect(int(input("\tPlease enter your own choice : ")))
    except ValueError as ve:
        print("Value Error! You must enter numbers, letters are not accepted.")
        redirectMain()
    except KeyboardInterrupt as ve:
        print("\n\tPlease do not use keyboard commands while program is running.")
        redirectMain()
###################################

def redirect(x): #This is to redirect from main function into a sub function # main gets x (The number) and then moves on to the function that does the work
    if x == 1: # redirects to 'add a new reading' function
        add_record()
    elif x == 2:
        update()
    elif x == 3:
        delete()
    elif x == 4:
        all_Readings()
    elif x == 5:
        return
    elif x == 6:
        dateType_Readings()
    elif x == 7:
        location_Readings()
    elif x == 8:
        return
    elif x == 9:
        return
    elif x == 0: # exits the function loop
        print("Thank you for using our program, have a good day.")
        exit()
    else: #automatically goes back to Main if doesnt fun
        print(f"{x} is not one of the choices, please enter a number between 0 and 9.")

        redirectMain()

###################################

def add_record(): # [1] Add a reading
    print("Smart Campus Management Application - Add a reading:\n=================================")
    timestamp = input("Enter timestamp: ")
    location = caseinsentivity(input("Enter location: "))
    sensorID =input("Enter Sensor ID:")
    if sensorID.upper not in list_Of_Sensors:
        print("Error: SensorID is not within the list of known sensors.")
        redirectMain()
    else:
        sensorID = sensorID.upper
    statusAlert = input("Enter Sensor Status/Alert: ")
    dataType = input("Enter Data Type: ")
    readingValue = input("Enter reading value: ")
    batteryLevel = input("Battery Level:")
    roomSize = input("Room Size:")
    installationDate = input("Installation Date:")
    addinfile = open('results.txt', 'a')
    addinfile.write('\n')
    addinfile.write(f'{timestamp},{location},{sensorID},{statusAlert},{dataType},{readingValue},{batteryLevel},{roomSize},{installationDate}')
    addinfile.close()
    print(". . . . .Record added.")
    redirectMain()

###################################

def update(): # [2] Update a reading
    print("Smart Campus Management Application - Update a reading:\n=================================")
    print("Please Enter reading's timestamp and Sensor ID.")
    timestamp = input("Enter timestamp: ")
    sensorID = input('Enter SensorID (case sensitive): ')
    exists = 0
    if sensorID in list_Of_Sensors:
        addinfile = open('results.txt', 'r')
        lines = addinfile.readlines()
        addinfile.close()
        for item in range(len(lines)):
            lines[item]=lines[item].strip()
        for line in lines:
            ttimestamp=line.split(",")[0]
            tsensorID=line.split(",")[2]
            statusAlert=line.split(",")[3]
            if ttimestamp == timestamp:
                if sensorID == tsensorID:
                    if statusAlert == 'Normal':
                        exists = exists + 1
                    else:
                        print(f'Record is listed as {statusAlert} you are not able to update it')
                        continue
                else:
                    continue
            else:
                continue
    else:
        print(f'Sensor ID: {sensorID} is not in the list of sensors.')
        redirectMain()
    if exists > 0:
                addinfile = open('results.txt', 'r')
                lines = addinfile.readlines()
                addinfile.close()
                for item in range(len(lines)):
                    lines[item]=lines[item].strip()
                tempfile = open('temp.txt', 'w')
                for line in lines:
                    tempfile.write(line+ '\n')
                tempfile.close()  
                os.remove('results.txt')
                addinfile = open('results.txt', 'w')
                for item in range(len(lines)):
                    lines[item]=lines[item].strip()
                for line in lines:
                        ttimestamp=line.split(",")[0]
                        tsensorID=line.split(",")[2]
                        statusAlert=line.split(",")[3]
                        if timestamp == ttimestamp:
                            if sensorID == tsensorID:
                                if statusAlert == 'Normal':
                                    timestamp =line.split(",")[0]
                                    location = line.split(",")[1]
                                    sensorID =line.split(",")[2]
                                    statusAlert = line.split(",")[3]
                                    dataType = line.split(",")[4]
                                    readingValue = input("Enter new reading value: ")
                                    batteryLevel = line.split(",")[6]
                                    roomSize = line.split(",")[7]
                                    installationDate = line.split(",")[8]
                                    addinfile.write(f'{timestamp},{location},{sensorID},{statusAlert},{dataType},{readingValue},{batteryLevel},{roomSize},{installationDate}' + '\n')
                                else:
                                    addinfile.write(line + '\n')
                            else:
                                addinfile.write(line + '\n')
                        else:
                            addinfile.write(line + '\n')
                addinfile.close()
                if os.path.exists('results.txt') == True:
                    if os.path.exists('temp.txt') == True:
                        os.remove('temp.txt')
                        print(". . . . .Record updated.")
                        redirectMain()
                    else:
                        redirectMain()
                else:
                    redirectMain()
    if exists < 1:
        print('Record was not found.')
        redirectMain()

###################################

def delete(): # [3] Delete a reading
    print("Smart Campus Management Application - Delete a reading:\n=================================")
    print("Please Enter reading's timestamp and ID.")
    timestamp = input("Enter timestamp: ")
    sensorID = input('Enter SensorID (case sensitive): ')
    if sensorID in list_Of_Sensors:
        addinfile = open('results.txt', 'r')
        lines = addinfile.readlines()
        addinfile.close()
        for item in range(len(lines)):
            lines[item]=lines[item].strip()
        tempfile = open('temp.txt', 'w')
        for line in lines:
            tempfile.write(line+ '\n')
        tempfile.close()  
        os.remove('results.txt')
        addinfile = open('results.txt', 'w')
        for item in range(len(lines)):
            lines[item]=lines[item].strip()
        for line in lines:
                ttimestamp=line.split(",")[0]
                tsensorID=line.split(",")[2]
                treadingValue=line.split(",")[2]

                if timestamp == ttimestamp:
                    if sensorID == tsensorID:
                        if treadingValue == 'n/a' or 'N/A':
                            print('Deletion was successful.')
                        else:
                            print(f'Couldn\'t delete the reading because reading value is {treadingValue}. You can only delete reading values that are n/a.')
                    else:
                        addinfile.write(line + '\n')
                else:
                    addinfile.write(line + '\n')
        
        addinfile.close()
        os.remove('temp.txt')
        redirectMain()
    else:
        print('Couldn\'t find sensor ID.')
        redirectMain()
        

    
###################################

def all_Readings(): # [4] Display all readings      
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
            print("-------------------|-----------|---------|-------------|---------------|------------------|-------------|-------------|------------------ ")
        else:
            print(f"{timestamp:19}|{location:11}|{sensorID:9}|{statusAlerts:13}|{dataType:15}|{value:18}|{batteryLevel:13}|{roomSize:13}|{installationDate:8}")

###################################

def statusAlerts_Readings(): # [5] Display all readings by Status/Alerts
    return

###################################

def dateType_Readings(): # [6] Display readings by a given data type"
    tdateType = dataType_caseinsentivity(input('Please enter data type to display: '))
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
                print("-------------------|-----------|---------|-------------|---------------|------------------|-------------|-------------|------------------ ")
            elif dataType == tdateType:
                print(f"{timestamp:19}|{location:11}|{sensorID:9}|{statusAlerts:13}|{dataType:15}|{value:18}|{batteryLevel:13}|{roomSize:13}|{installationDate:8}")
    redirectMain()


###################################

def location_Readings(): # [7] Display readings in a given location
    tlocation = caseinsentivity(input('Please enter location to display: '))
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
                print("-------------------|-----------|---------|-------------|---------------|------------------|-------------|-------------|------------------ ")
            elif location == tlocation:
                print(f"{timestamp:19}|{location:11}|{sensorID:9}|{statusAlerts:13}|{dataType:15}|{value:18}|{batteryLevel:13}|{roomSize:13}|{installationDate:8}")


###################################

def caseinsentivity(location): # Checks for location while being caseinsentive
    location = str.casefold(location)
    if location not in list_Of_Locations: #Checks validity
        print(f"{location} is not accepted. Please only use valid location")
        print('Valid locations are (' + ','.join(list_Of_Locations) +')' )
        redirectMain()
    location = str.capitalize(location)
    return location

###################################

def dataType_caseinsentivity(dataType):
    str.casefold(dataType)
    if dataType not in list_Of_DataTypes:
        print(f'{dataType} is not valid. Please only use valid data types')
        print('Valid data types are (' + ','.join(list_Of_DataTypes) +')')
        redirectMain()
    dataType = str.capitalize(dataType)
    if dataType == 'Co2 level':
        dataType = "CO2 Level"
    elif dataType == "Light intensity":
        dataType == 'Light Intensity'
    return dataType
        

   
###################################
      
def redirectMain(): # Instead of repeating redirection to main, make it one function.
    print("Returning to main. . .")
    main()


###################################

def lister():
    global list_Of_Sensors 
    global list_Of_Locations
    global list_Of_DataTypes
    read = open('results.txt', 'r')
    lines = read.readlines()
    read.close()
    for item in range(len(lines)):
        lines[item]=lines[item].rstrip('\n')
    for line in lines:
            Location=line.split(",")[1]
            SensorID=line.split(",")[2]
            dataType=line.split(",")[4]
            if SensorID != "Sensor ID":
                if SensorID not in list_Of_Sensors:
                    list_Of_Sensors.append(SensorID)
            if Location != "Location":
                Location = str.casefold(Location)
                if Location not in list_Of_Locations:
                    list_Of_Locations.append(Location)
            if dataType != "Data Type":
                dataType = str.casefold(dataType)
                
                if dataType not in list_Of_DataTypes:
                    list_Of_DataTypes.append(dataType)
                    
# # PLEASE RUN CODE BELOW HERE
list_Of_Sensors = []
list_Of_Locations = []
list_Of_DataTypes = []

if os.path.exists('results.txt') == True: # Checks if results text file exists
    lister()
    main()
elif os.path.exists('temp.txt') == True: # Check if the temp file exists
    print('File recovery is running.')
    print('Results file doesn\'t exist however temp results file exists.')
    check = input('Do you wish to use it?')
    if str.upper(check) == 'Y':
        os.rename('temp.txt', 'results.txt') # Makes the temp file the new main file
        print('File has been created.')
        lister()
        main()
    else:
        redirect(0)
    main()
else: # If both files do not exists it creates a new file with no readings if the user wants. 
    print("Results file file doesn't exists . Please try to recover it.")
    check = input('Please type Y if you wish to create a new readings file, else type N or anything else.')
    if str.upper(check) == 'Y':
        createfile = open('results.txt', 'w') 
        createfile.write('Timestamp,Location,Sensor ID,Status/Alerts,Data Type,Value,Battery Level,Room Size,Installation Date')
        createfile.close
        print('File has been created.')
    else:
        redirect(0)