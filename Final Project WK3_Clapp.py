# Final Project WK3 - Temperature Conversion
from datetime import datetime

print("miccla8284 Spreadsheet Automation Menu.")

#Define the conversion function, round to 2 decimal places
def convertData(data):
    convertedValue = (data - 32)*5/9
    return round(convertedValue, 2)

#Define the input- specify *F entry for *C conversion
def getInput():
    entries = int(input("How many entries are you inputting?"))
    for i in range(entries):
        date = input("Enter a date: ")
        value = float(input("Enter the highest temp in Farenheit for the inputted date: "))

        #Use numerical value argument, return a converted Celsius value
        convertedValue = convertData(value)

        print("The following was saved at", datetime.now(), ":")
        print(date + "," + str(value) + "," + str(convertedValue))
        
print("Choose a number from the following options")
# Required Menu options stored as a list
menu_options = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report"]

# Use for loop to show menu options
for option in menu_options:
    print(option)

#stores the inputted option into the variable
user_choice = input()

#use if-else to validate option selected
if user_choice == "1" or user_choice == "2" or user_choice =="3":
    print("You selected", user_choice, "at", str(datetime.now()))
    if user_choice == "1":
        getInput()
    else:
        print("Error: The chosen functionality is not implemented yet")
else:
    print("Error: Invalid choice selected")
