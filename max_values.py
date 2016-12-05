import os
import openpyxl

#Prompt for directory name to find max values in text files
directory = input("Please enter the file directory: ")

#Create empty excel workbook with 1 empty worksheet
wb = openpyxl.Workbook('MaxValues.xlsx')
ws = wb.create_sheet()

def clean_line(line):
    return int(line.strip(';\n'))

#checks for existence of directory given by user
if os.path.lexists(directory):
    print(os.path.split(directory))

    #iterates over files in given directory
    for path, dirs, files in os.walk(directory):
        #opens files one by one
        for blah in files:
            #print("Opening:" + blah)
            filepath = os.path.join(directory, blah)
            #print("Poopinggggg: " + filepath)
            f = open(filepath)

            numbers = map(clean_line, f.readlines())

            #for line in f.readlines():
            #    strip_line = line.strip(';\n')
            #    numbers.append(int(strip_line))
            print(max(numbers))

        #wb.save("MaxValues.xlsx")
        #wb.close("MaxValues.xlsx")
else:
    print("That pathway,"+ directory + " is no good.")


print(os.path.dirname(directory))
