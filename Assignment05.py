# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
# ChangeLog (Who,When,What):
# Chani,8.8.21,Created script
# Chani,8.9.21,Edited for aesthetic
# Chani,8.9.21,Moved any constants to the Data section and fixed errant indentations
# Chani,8.9.21,Edited Option 4, 3, and 1
# Chani,8.10.21,Edited for spelling errors and Option 1 and 4
# Chani,8.10.21,Added pauses for user flow
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None   # An object that represents a file
strFile = "ToDolist.txt"
strData = ""   # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
save = ''      # Capture of user option to save
delChoice = '' # Capture of user option to delete



# -- Processing -- #
#Load data from text file ToDoList.txt into a python list of dictionary rows:
print("To Do List:")                            # < some bs the dev added
objFile = open(strFile, "r")                    #< opens ToDoList.txt
for row in objFile:                             #< fetches ToDoList 1 row at a time
    lstRow = row.split(",")                     #< adds spaces and commas to make it pretty
    dicRow = {"priority":lstRow[0].strip(), "task":lstRow[1].strip()}
    print(dicRow['priority'] + ' - ' + dicRow['task'])  #< prints the ToDoList row by row
    lstTable.append(dicRow)                     #< adds these dictionaries to the current list


# -- Input/Output -- #
#DISPLAY a menu of choices to the user:
    # Overarching loop checks for options and breaks at 5, but what if option not valid?
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  #adds a new line for looks


    #OPTION 1) Show the current items in the table:
    if (strChoice.strip() == '1'):
        index = 0
        print("*  Viewing To Do list:\n\tPriority - Task")
        for row in lstTable:                                #< fetches each item in the list table one at a time
            print((index + 1), ") ", row['priority']," - ", row['task'])
            index += 1                                      #< adds numbers making it a numbered list
        input("enter to continue")

    #OPTION 2) Add a new item to the list/Table:
    elif (strChoice.strip() == '2'):
        print("Record a chore, errand, or aspiration...\n\t(Example: \"Put out that kitchen fire - "
              "high priority)\"\n")
        task = input("\tDescribe the Task you're considering doing: ")      #< assigns a key and value
        priority = input("\tOn a relative scale, where would you"           #< assigns a key and value
                         " prioritize this task?: ")
        dicRow = {"priority":priority, "task":task}                         #< adds those to a dictionary
        input("YOU HAVEN'T ALREADY " + dicRow["task"] + "!!!??? O.O\n\tI'll add it to your To Do list "
                "right away!")         # ^ Im aware that the tense will almost always be improper. I find it funny.
        #^ script pause
        lstTable.append(dicRow)                                             #< adds this item(dic) to the list
        continue

    #OPTION 3) - Remove a new item from the list/Table:
    elif (strChoice.strip() == '3'):
        print("Which task (number) would you like to delete?:")
        while True:                                       #< yes, another While loop! will continue as long as .isnumeric
        #Prints out the list:
            index = 0                                         # < set the index here and not outside the "while True" X<
            for row in lstTable:                                #< fetches each item in the list table one at a time
                print(index, ") ", row['priority']," - ", row['task'])
                index += 1
            # Get users choice from that list:
            delChoice = input("Delete number: ").strip()      # < sets choice and removes any extra space
            if (not delChoice.isnumeric()):
                input("\nThat cannot be deleted. Lets try again, boss.")
                break
            if (int(delChoice) < len(lstTable) and int(delChoice) >= 0):  # < if choice is numeric and also on the list,
                del lstTable[int(delChoice)]                              # < deletes it
                continue                                        # < comes back the list and resets the variable? yes
            else:
                print("\n  *Pick a number from 0 to " , (len(lstTable) - 1), ", please.*")  # < not cheeky this time
                continue                                        # < comes back the list and resets the variable?

    #OPTION 4 - Save tasks to the ToDoList.txt file:
    elif (strChoice.strip() == '4'):
        while True:                                #< sets the loop parameters to anything but 'n'
            save = input("Would you like to save this list ('y' or 'n')?: ")  #< gets and saves user input
            if (save.lower().strip() == 'y'):               #< removes spaces and lowers input (invisible to user)
                objFile = open(strFile, "w")
                #reference option 1 about how to print list
                for dicRow in lstTable:
                    objFile.write(dicRow["priority"] + ',' + dicRow["task"] + '\n')
                objFile.close()
                input("Your Data has been Saved!") #< pauses
                break
            else: break

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Program will now close.")         #< lets try something simple before we overthink it
        break  # and Exit the program            #< this breaks from the whole program, yes?
        # ^ I might add a failsafe later

#Oh! If you dont specify that youd like to close (option 5), it just repeats the loop.