def main(): # This is the main interfere for everything else
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
        main()

###################################

def redirect(x): #This is to redirect from main function into a sub function # main gets x (The number) and then moves on to the function that does the work
    if x == 1: # redirects to add reading function
        addReading()
    elif x == 2:
        return
    elif x == 3:
        return
    elif x == 4:
        return
    elif x == 5:
        return
    elif x == 6:
        return
    elif x == 7:
        return
    elif x == 8:
        return
    elif x == 9:
        return
    elif x == 0: # exits the function loop
        print("Thank you for using our program, have a good day.")
    else: 
        print(f"{x} is not one of the choices, please enter a number between 0 and 9.")
        print("Returning to main...")
        main()

###################################


def addReading(): # [1] Add a reading
    print("Smart Campus Management Application - Add a reading:\n=================================")
    input("Enter timestamp: ")
    input("Enter location: ")
    input("Enter Sensor ID:")
    input("Enter Sensor Status/Alert: ")
    input("Enter Data Type: ")
    input("Enter reading value: ")
    input("Battery Level:")
    input("Room Size:")
    input("Installation Date:")
    print(". . . . .Record added.")
    
###################################
    
# def








     
# # PLEASE RUN CODE BELOW HERE
main()
