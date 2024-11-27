import turtle, math, random, os, datetime

def main(): # This is the main interfere for everything else - A
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
        shape_add() # done
    elif x == 2:
        shape_update() # done
    elif x == 3:
        shape_delete() # done 
    elif x == 4:
        list_all() # done 
    elif x == 5:
        list_category() # done
    elif x == 6:
        draw_shape()  # done
    elif x == 7:
        statistics() # not yet
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
    print('Please enter the information for the new shape.\n')
    add_reading_Type = input(f'Enter value for Type: ')
    add_reading_FillColor = input(f'Enter value for Fill Colour: ')
    add_reading_BorderColor = input(f'Enter value for Border Colour: ')
    add_reading_BorderThickness = input(f'Enter value for Border Thickness: ')
    add_reading_Length = input(f'Enter value for Length: ')
    add_reading_Width = input(f'Enter value for Width: ')
    add_reading_Size = input(f'Enter value for Size: ')
    add_reading_Position = input(f'Enter value for Position: ')
    add_reading_Description = input(f'Enter value for Description: ')

    Shapecodes_list = []
    with open('shapes.txt', 'r') as infile:
            readings = infile.readlines()
    for i in range(len(readings)):
            readings[i]=readings[i].strip()
    for reading in readings: 
            reading_Type,reading_FillColor,reading_BorderColor,reading_BorderThickness,reading_Length,reading_Width,reading_Size,reading_Position,reading_Description,reading_ShapeCode,reading_CreationTime= reading.split('|')
            if reading_ShapeCode != 'ShapeCode':
                Shapecodes_list.append(int(reading_ShapeCode))
    add_reading_ShapeCode = (max(Shapecodes_list) + 1)

    time = datetime.datetime.now()
    add_reading_CreationTime = time.strftime('%Y-%m-%d %H:%M')

    with open('shapes.txt', 'a') as outfile:
        outfile.write(f'\n{add_reading_Type}|{add_reading_FillColor}|{add_reading_BorderColor}|{add_reading_BorderThickness}|{add_reading_Length}|{add_reading_Width}|{add_reading_Size}|{add_reading_Position}|{add_reading_Description}|{add_reading_ShapeCode}|{add_reading_CreationTime}')
    print('Value added.\n')
    redirectMain()

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
                ui_Updatevalue = input('''Type the number according to the value you want to change while seperating them with a space
Type[1] FillColor[2] BorderColor[3] BorderThickness[4] Length[5] Width[6] Size[7] Position[8] Description[9] ShapeCode[10] CreationTime[11]
''').split(' ')
                if '1' in ui_Updatevalue:
                    reading_Type = input(f'Enter new value for Type. Current value is {reading_Type}: ')
                if '2' in ui_Updatevalue:
                    reading_FillColor = input(f'Enter new value for Fill Colour. Current value is {reading_FillColor}: ')
                if '3' in ui_Updatevalue:
                    reading_BorderColor = input(f'Enter new value for Border Colour. Current value is {reading_BorderColor}: ')
                if '4' in ui_Updatevalue:
                    reading_BorderThickness = input(f'Enter new value for Border Thickness. Current value is {reading_BorderThickness}: ')
                if '5' in ui_Updatevalue:
                    reading_Length = input(f'Enter new value for Length. Current value is {reading_Length}: ')
                if '6' in ui_Updatevalue:
                    reading_Width = input(f'Enter new value for Width. Current value is {reading_Width}: ')
                if '7' in ui_Updatevalue:
                    reading_Size = input(f'Enter new value for Size. Current value is {reading_Size}: ')
                if '8' in ui_Updatevalue:
                    reading_Position = input(f'Enter new value for Position. Current value is {reading_Position}: ')
                if '9' in ui_Updatevalue:
                    reading_Description = input(f'Enter new value for Description. Current value is {reading_Description}: ')
                if '10' in ui_Updatevalue:
                    reading_ShapeCode = input(f'Enter new value for Shape Code. Current value is {reading_ShapeCode}: ')
                if '11' in ui_Updatevalue:
                    reading_CreationTime = input(f'Enter new value for Creation Time. Current value is {reading_CreationTime}: ')

                outfile.write(f'{reading_Type}|{reading_FillColor}|{reading_BorderColor}|{reading_BorderThickness}|{reading_Length}|{reading_Width}|{reading_Size}|{reading_Position}|{reading_Description}|{reading_ShapeCode}|{reading_CreationTime}')
                print('Value has been updated.')
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
                print('Value deleted.')
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
    

    redirectMain() # loops back to main


###################################

def list_category():
    with open('shapes.txt', 'r') as infile:
        readings = infile.readlines()
    #
    check_if_exists = 'not'
    ui_readingType = input('Please type category of shapes to be listed : ')
    #
    for i in range(len(readings)):
        readings[i]=readings[i].strip()
    for reading in readings:
        reading_Type,reading_FillColor,reading_BorderColor,reading_BorderThickness,reading_Length,reading_Width,reading_Size,reading_Position,reading_Description,reading_ShapeCode,reading_CreationTime= reading.split('|')
        if reading_Type == ui_readingType:
            print(reading)
            check_if_exists = 'True'
        else:
            pass
    if check_if_exists == 'not':
        print('No values were found')
    
    redirectMain() # loops back to main

###################################

def draw_shape():
    while True:
            with open("shapes.txt", "r") as file:
                lines = file.readlines()
                if len(lines) < 2:
                    print("No shapes found to draw!")
                    return

            attribute = input("Enter shape type or attribute to filter (e.g., circle, red, etc.): ").strip()

            shapes_to_draw = []
            for line in lines[1:]:
                if attribute.lower() in line.lower():
                    shapes_to_draw.append(line.strip().split("|"))

            if not shapes_to_draw:
                print("No shapes found matching the attribute.")
                return

            screen = turtle.Screen()
            screen.title("Turtle Shapes Application")
            turtle.speed(0)

            for shape in shapes_to_draw:
                shape_type = shape[0].lower()
                fill_color = shape[1]
                border_color = shape[2]
                border_thickness = int(shape[3])
                length = shape[4]
                width = shape[5]
                size = shape[6]
                position = eval(shape[7])
                rotation = int(shape[8])

                turtle.penup()
                turtle.goto(position)
                turtle.pendown()
                turtle.pensize(border_thickness)
                turtle.pencolor(border_color)
                turtle.fillcolor(fill_color)
                turtle.begin_fill()

                if shape_type == "circle":
                    turtle.circle(int(size))
                elif shape_type == "square":
                    for _ in range(4):
                        turtle.forward(int(size))
                        turtle.left(90)
                elif shape_type == "rectangle":
                    for _ in range(2):
                        turtle.forward(int(length))
                        turtle.left(90)
                        turtle.forward(int(width))
                        turtle.left(90)
                elif shape_type == "triangle":
                    for _ in range(3):
                        turtle.forward(int(size))
                        turtle.left(120)
                elif shape_type == "oval":
                    # Draw an ellipse by drawing two arcs with different radii
                    radius1 = int(length)  # Use length as the width of the ellipse
                    radius2 = int(width)  # Use width as the height of the ellipse
                    turtle.setheading(0)
                    for _ in range(2):
                        turtle.circle(radius1, 90)  # Draw the top half
                        turtle.circle(radius2, 90)  # Draw the bottom half
                else:
                    print(f"Shape type '{shape_type}' is not supported!")
                    continue

                turtle.end_fill()

                if rotation != 0:
                    turtle.setheading(rotation)

            turtle.done

            with open("records.txt", "a") as records_file:
                records_file.write("Type|FillColor|BorderColor|BorderThickness|Length|Width|Size|Position|Description|ShapeCode|CreationTime\n")
                for shape in shapes_to_draw:
                    records_file.write("|".join(shape) + "\n")

            print("Shapes drawn successfully and saved to records.txt!")
            repeat = input("Do you want to draw more shapes? (yes/no): ").strip().lower()
            if repeat != "yes":
                redirectMain()
###################################

def statistics():
        print('''Please specify what you want to analyze
[1] Type [2] Color [3] Size [4] All [0] To cancel''')
        ui_requirements = input('Please enter your option: ').split('123')
        list_reading_Type = [] # initializiation for all local values/list/dict
        list_reading_Colours = []
        list_reading_size = []
        list_reading_totalcount = 0
        list_color_checked = []
        list_type_checked = []
        dictionary_color = dict()
        dictionary_type = dict() 
        if '0' != ui_requirements: # makes sure user didnt want to quit
##################################################################################################################################################################
                if '1' in ui_requirements: # SAME AS 4
                    with open('shapes.txt', 'r') as infile: # just gets readings
                        list_of_valid_shapes = ['circle','square','triangle','rectangle','oval']
                        while True:
                            ui_condition = input('Which type of shape would you like to anaylize: ')
                            if ui_condition in list_of_valid_shapes:
                                break
                            else:
                                print(f'''{ui_condition} is not a valid option.
Valid options are: {', '.join(list_of_valid_shapes)}''')
                        readings = infile.readlines()
                        for i in range(len(readings)):      # prepares readings
                                readings[i]=readings[i].strip()
                        for reading in readings:  # General Code for specific values in reading
                                reading_Type,reading_FillColor,reading_BorderColor,reading_BorderThickness,reading_Length,reading_Width,reading_Size,reading_Position,reading_Description,reading_ShapeCode,reading_CreationTime= reading.split('|')
                                if reading_Type == ui_condition: # Condition
                                        list_reading_Type.append(reading_Type) # Compiles all types into list
                                        list_reading_Colours.append(reading_FillColor) # Complies all colors into list
                                        list_reading_size.append(int(reading_Size)) # complies all sizes into a list after turning them into int
                                        list_reading_totalcount += 1 # counts
                        list_size_avg = sum(list_reading_size)/ len(list_reading_size) # Gets average size
                        list_size_min = min(list_reading_size) # Gets smallest size
                        list_size_max = max(list_reading_size) # Gets largest size
                        for item in list_reading_Colours: # uses color list to turn into a dictionary
                                if item not in list_color_checked:
                                        list_color_checked.append(item)
                                        dictionary_color[item]=1
                                elif item in list_color_checked:
                                        dictionary_color[item] = dictionary_color[item] + 1
                        dictionary_color_loader = ['Distribution of Colors:'] # uses dictionary and turns it into a string
                        for colours in dictionary_color:
                                dictionary_color_loader.append(f'-{colours}: {dictionary_color.get(colours)}')
                        loaded_color_list = ('\n'.join(dictionary_color_loader)) # resulting useable string from dictionary

                                                # complies all data into a value
                        anyalisis_all = f'''Statistics for Shapes of Type: {ui_condition}
Total Count: {list_reading_totalcount}

{loaded_color_list}

Average Size: {list_size_avg}
Smallest Size: {list_size_min}
Largest Size: {list_size_max}'''
                        print(anyalisis_all) # prints 'anaylsis
                        ui_anaylsis = input('\nType Y for the statistics to be written in a text file: ') # gets user confirmation
                        
                        if ui_anaylsis == 'Y' or ui_anaylsis == 'y': # turns anyalsis into a text file
                                with open('analysis.txt', 'w') as infile:
                                        infile.write(anyalisis_all)
                                print('Anaylsis.txt file has been created.')
##################################################################################################################################################################
                elif '2' in ui_requirements: # SAME AS 4
                        ui_requirement = input('Which color shape would you like to anaylize: ')
                        readings = infile.readlines()
                        for i in range(len(readings)):      # prepares readings
                                readings[i]=readings[i].strip()
                        for reading in readings:  # General Code for specific values in reading
                                reading_Type,reading_FillColor,reading_BorderColor,reading_BorderThickness,reading_Length,reading_Width,reading_Size,reading_Position,reading_Description,reading_ShapeCode,reading_CreationTime= reading.split('|')
                                if reading_FillColor == ui_requirement: # Condition
                                        list_reading_Type.append(reading_Type) # Compiles all types into list
                                        list_reading_size.append(int(reading_Size)) # complies all sizes into a list after turning them into int
                                        list_reading_totalcount += 1 # counts
                                        
                        list_size_avg = sum(list_reading_size)/ len(list_reading_size) # Gets average size
                        list_size_min = min(list_reading_size) # Gets smallest size
                        list_size_max = max(list_reading_size) # Gets largest size
                        for item in list_reading_Type: # uses type list to turn into a dictionary
                                if item not in list_type_checked:
                                        list_type_checked.append(item)
                                        dictionary_type[item]=1
                                elif item in list_type_checked:
                                        dictionary_type[item] = dictionary_type[item] + 1
                        dictionary_type_loader = ['Distribution of Types:'] # similar to colors
                        for type in dictionary_type:
                                dictionary_type_loader.append(f'-{type}: {dictionary_type.get(type)}')
                        
                        loaded_type_list = ('\n'.join(dictionary_type_loader))
                        # complies all data into a value
                        anyalisis_all = f'''Statistics for Shapes of Color: {ui_requirement}
Total Count: {list_reading_totalcount}

{loaded_type_list}

Average Size: {list_size_avg}
Smallest Size: {list_size_min}
Largest Size: {list_size_max}'''
                        print(anyalisis_all) # prints 'anaylsis
                        ui_anaylsis = input('\nType Y for the statistics to be written in a text file: ') # gets user confirmation
                        
                        if ui_anaylsis == 'Y' or ui_anaylsis == 'y': # turns anyalsis into a text file
                                with open('analysis.txt', 'w') as infile:
                                        infile.write(anyalisis_all)
                                print('Anaylsis.txt file has been created.')
##################################################################################################################################################################
                elif '3' in ui_requirements: # SAME AS 4
                        pass
##################################################################################################################################################################
                elif '4' in ui_requirements: ###### START CODE FOR NUMBER 4. ALL OTHERS ARE SIMILAR TO 4 BUT HAVE REQUIREMENTS
                        with open('shapes.txt', 'r') as infile: # just gets readings
                                readings = infile.readlines()
                        for i in range(len(readings)):      # prepares readings
                                readings[i]=readings[i].strip()
                        for reading in readings:  # General Code for specific values in reading
                                reading_Type,reading_FillColor,reading_BorderColor,reading_BorderThickness,reading_Length,reading_Width,reading_Size,reading_Position,reading_Description,reading_ShapeCode,reading_CreationTime= reading.split('|')
                                if reading_Type != 'Type': # Condition
                                        list_reading_Type.append(reading_Type) # Compiles all types into list
                                        list_reading_Colours.append(reading_FillColor) # Complies all colors into list
                                        list_reading_size.append(int(reading_Size)) # complies all sizes into a list after turning them into int
                                list_reading_totalcount += 1 # counts
                        list_size_avg = sum(list_reading_size)/ len(list_reading_size) # Gets average size
                        list_size_min = min(list_reading_size) # Gets smallest size
                        list_size_max = max(list_reading_size) # Gets largest size
                        for item in list_reading_Colours: # uses color list to turn into a dictionary
                                if item not in list_color_checked:
                                        list_color_checked.append(item)
                                        dictionary_color[item]=1
                                elif item in list_color_checked:
                                        dictionary_color[item] = dictionary_color[item] + 1
                        for item in list_reading_Type: # uses type list to turn into a dictionary
                                if item not in list_type_checked:
                                        list_type_checked.append(item)
                                        dictionary_type[item]=1
                                elif item in list_type_checked:
                                        dictionary_type[item] = dictionary_type[item] + 1
                        dictionary_color_loader = ['Distribution of Colors:'] # uses dictionary and turns it into a string
                        for colours in dictionary_color:
                                dictionary_color_loader.append(f'-{colours}: {dictionary_color.get(colours)}')
                        loaded_color_list = ('\n'.join(dictionary_color_loader)) # resulting useable string from dictionary
                        dictionary_type_loader = ['Distribution of Types:'] # similar to colors
                        for type in dictionary_type:
                                dictionary_type_loader.append(f'-{type}: {dictionary_type.get(type)}')
                        
                        loaded_type_list = ('\n'.join(dictionary_type_loader))
                        # complies all data into a value
                        anyalisis_all = f'''Statistics for all Shapes
Total Count: {list_reading_totalcount}

{loaded_color_list}

{loaded_type_list}

Average Size: {list_size_avg}
Smallest Size: {list_size_min}
Largest Size: {list_size_max}'''
                        print(anyalisis_all) # prints 'anaylsis
                        ui_anaylsis = input('\nType Y for the statistics to be written in a text file: ') # gets user confirmation
                        
                        if ui_anaylsis == 'Y' or ui_anaylsis == 'y': # turns anyalsis into a text file
                                with open('analysis.txt', 'w') as infile:
                                        infile.write(anyalisis_all)
                                print('Anaylsis.txt file has been created.')
##################################################################################################################################################################
        redirectMain()


###################################

main()
