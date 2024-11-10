import turtle, math, random, os

def main(): # This is the main interfere for everything else
    print("\n\t\tTurtle Shapes Application")
    print("\t\t   [1] Add shape")
    print("\t\t   [2] Update shape")
    print("\t\t   [3] Delete shape")
    print("\t\t   [4] List all shapes")
    print("\t\t   [5] List by category")
    print("\t\t   [6] Draw shape")
    print("\t\t   [7] Statistics")
    print(" ")
    print("\t\t   [0] Exit")
    try: # This is to catch Value Errors from invalid input statements, if caught, restarts.
        redirect(int(input("\tPlease enter your choice : ")))
    except ValueError as ve:
        print("Value Error! You must enter numbers, letters are not accepted.")
        redirectMain()
    except KeyboardInterrupt as ve:
        print("\n\tPlease do not use keyboard commands while on input.")
        redirectMain()

###################################

def redirect(x): #This is to redirect from main function into a sub function # main gets x (The number) and then moves on to the function that does the work
    if x == 1: # redirects to 'add a new reading' function
        shape_add() # not yet (input validation if want)
    elif x == 2:
        shape_update() # done (input validation if want)
    elif x == 3:
        shape_delete() # done (input validation if want)
    elif x == 4:
        list_all() # done 
    elif x == 5:
        list_category() # redoing very ineffiecent 
    elif x == 6:
        shape_draw()  # not my job
    elif x == 7:
        statistics() # ask teacher 
    elif x == 0: # exits the function loop
        print("Thank you for using our program, have a good day.")
        exit()
    else: #automatically goes back to Main.
        print(f"{x} is not one of the choices, please enter a number between 0 and 7.")

        redirectMain()

###################################

def redirectMain(): # Instead of repeating redirection to main, make it one function. Also allows main to refer to main.
    main()

###################################

def shape_add():
    pass

###################################

def shape_update():
    ui_UpdateCode = input('Please provide the code of the shape you wish to update: ')

    with open('shapes.txt', 'r') as infile:
        readings = infile.readlines()
    with open('shapes_temp.txt', 'w') as outfile:
        for reading in readings:
            update_code = reading.split('|')[9]
            if update_code == ui_UpdateCode:
                reading_Type,reading_FillColor,reading_BorderColor,reading_BorderThickness,reading_Length,reading_Width,reading_Size,reading_Position,reading_Description,reading_ShapeCode,reading_CreationTime= reading.split('|')
                ## for each
                ui_verify = input('Do you want to change fill color? Y or N : ')
                if ui_verify == 'Y' or ui_verify == 'y':
                    reading_FillColor = input('What do you want to set the fill color as: ')
               
                ui_verify = input('Do you want to change border color? Y or N : ')
                if ui_verify == 'Y' or ui_verify == 'y':
                    reading_BorderColor = input('What do you want to set the border color as: ')
                
                ui_verify = input('Do you want to change border thickness? Y or N : ')
                if ui_verify == 'Y' or ui_verify == 'y':
                    reading_BorderThickness = input('What do you want to set the border thickness as: ')
                
                ui_verify = input('Do you want to change length? Y or N : ')
                if ui_verify == 'Y' or ui_verify == 'y':
                    reading_Length = input('What do you want to set the length as: ')
                
                ui_verify = input('Do you want to change width? Y or N : ')
                if ui_verify == 'Y' or ui_verify == 'y':
                    reading_Width = input('What do you want to set the width as: ')
                
                ui_verify = input('Do you want to change size? Y or N : ')
                if ui_verify == 'Y' or ui_verify == 'y':
                    reading_Size = input('What do you want to set the size as: ')
                
                ui_verify = input('Do you want to change the position? Y or N : ')
                if ui_verify == 'Y' or ui_verify == 'y':
                    reading_Position = input('What do you want to set the position as: ')

                ui_verify = input('Do you want to change the description? Y or N : ')
                if ui_verify == 'Y' or ui_verify == 'y':
                    reading_Description = input('What do you want to set the description as: ')
                
                ui_verify = input('Do you want to change fill color? Y or N : ')
                if ui_verify == 'Y' or ui_verify == 'y':
                    reading_CreationTime = input('What do you want to set the fill color as?')

                outfile.write(f'{reading_Type}|{reading_FillColor}|{reading_BorderColor}|{reading_BorderThickness}|{reading_Length}|{reading_Width}|{reading_Size}|{reading_Position}|{reading_Description}|{reading_ShapeCode}|{reading_CreationTime}')
            else:
                outfile.write(reading)
    os.remove('shapes.txt')
    os.rename('shapes_temp.txt', 'shapes.txt')
    
    redirectMain() # loops back to main 

###################################

def shape_delete():
    ui_DeleteCode = input('Please provide the code of the shape you wish to delete: ')
    with open('shapes.txt', 'r') as infile:
        readings = infile.readlines()
    with open('shapes_temp.txt', 'w') as outfile:
        for reading in readings:
            delete_code = reading.split('|')[9]
            if delete_code == ui_DeleteCode:
                pass
            else:
                outfile.write(reading)
    os.remove('shapes.txt')
    os.rename('shapes_temp.txt', 'shapes.txt')
    
    redirectMain() # loops back to main 

###################################

def list_all():
    with open('shapes.txt', 'r') as infile:
        readings = infile.readlines()
    for i in range(len(readings)):
        readings[i]=readings[i].strip()
    for reading in readings:
        reading_Type,reading_FillColor,reading_BorderColor,reading_BorderThickness,reading_Length,reading_Width,reading_Size,reading_Position,reading_Description,reading_ShapeCode,reading_CreationTime= reading.split('|')
        if reading_Type != 'Type':
            print(f'{reading_Type:9}|{reading_FillColor:9}|{reading_BorderColor:11}|{reading_BorderThickness:15}|{reading_Length:6}|{reading_Width:5}|{reading_Size:4}|{reading_Position:9}|{reading_Description:11}|{reading_ShapeCode:9}|{reading_CreationTime:16}')
        else:
            print(f'{reading_Type:9}|{reading_FillColor:9}|{reading_BorderColor:11}|{reading_BorderThickness:15}|{reading_Length:6}|{reading_Width:5}|{reading_Size:4}|{reading_Position:9}|{reading_Description:11}|{reading_ShapeCode:9}|{reading_CreationTime:16}')

            print(f"{'-'*9}|{'-'*9}|{'-'*11}|{'-'*15}|{'-'*6}|{'-'*5}|{'-'*4}|{'-'*9}|{'-'*11}|{'-'*9}|{'-'*16}")
    
    ui_confirm = input('\nType (Y) to go back to main, anything else to quit : ')
    if ui_confirm == 'y' or ui_confirm == 'Y':
        redirectMain() # loops back to main
    else:
        redirect(0)

def list_category():
    with open('shapes.txt', 'r') as infile:
        readings = infile.readlines()
    #
    ui_readingType = input('Please type category of shapes to be listed : ')
    #
    for i in range(len(readings)):
        readings[i]=readings[i].strip()
    for reading in readings:
        reading_Type,reading_FillColor,reading_BorderColor,reading_BorderThickness,reading_Length,reading_Width,reading_Size,reading_Position,reading_Description,reading_ShapeCode,reading_CreationTime= reading.split('|')
        if reading_Type == ui_readingType:
            print(reading)
        else:
            pass
    
    redirectMain() # loops back to main

###################################

def shape_draw():
    pass

###################################

def statistics():
    pass

###################################

main()
