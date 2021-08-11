# -------------------------------------------------- #
# Title: Listing 9
# Description: Writing and Reading Data from a file
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Chani,8/7/21,Changed rows from lists to dictionaries
# -------------------------------------------------- #

# Declare my variables
strChoice = '' # User input
dicRow = {}
lstTable = []# list of data
strFile = 'HomeInventory.txt'  # data storage file
objFile = None  # file handle

# Get user Input
while(True):
    print("Write or Read file data, then type 'Exit' to quit!")
    strChoice = input("Choose to [W]rite or [R]ead data: ")
    

    # Process the data
    if (strChoice.lower() == 'exit'): break
    elif (strChoice.lower() == 'w'):
        # List to Dictionary
        objFile = open(strFile, "w")
        dicRow = {"item":"Lamp", "value":"$30"}
        objFile.write(dicRow["item"] + ',' + dicRow["value"] + '\n')
        dicRow = {"item":"End Table", "value":"$70"}
        objFile.write(dicRow["item"] + ',' + dicRow["value"] + '\n')
        objFile.close()
    elif (strChoice.lower() == 'r'):
        # File to List
        objFile = open(strFile, "r")
        for row in objFile:
            dicRow = row.split(",") # Returns a list!
            print(dicRow[0] + '|' + dicRow[1].strip())
        objFile.close()
    else:
        print('Please choose either W or R!')
