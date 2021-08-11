# -------------------------------------------------- #
# Title: Lab 5-1
# Description: Writing and Reading Data from a file
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Chani,8/6/21, Added read/write to file code
# -------------------------------------------------- #

# Declare my variables
strChoice = '' # User input
lstRow = []  # list of data
strFile = 'Lab5-1.txt'  # data storage file
objFile = None  # file handle

# Get user Input
while(True):
    print("Write or Read file data, then type 'Exit' to quit!")
    strChoice = input("Choose to [W]rite or [R]ead data: ")

    # Process the data
    if (strChoice.lower() == 'exit'): break
    elif (strChoice.lower() == 'w'):
        objFile = open(strFile, "w")
        lstRow = ["Item", "Value"]
        objFile.write(lstRow[0] + ',' + lstRow[1] + '\n')
        lstRow = ["Lamp", "$30"]
        objFile.write(lstRow[0] + ',' + lstRow[1] + '\n')
        lstRow = ["End Table", "$60"]
        objFile.write(lstRow[0] + ',' + lstRow[1] + '\n')
        objFile.close()
    elif (strChoice.lower() == 'r'):
        # File to List
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",")
            print(lstRow[0] + '|' + lstRow[1].strip())
        objFile.close()
    else:
        print('Please choose either W or R!')

