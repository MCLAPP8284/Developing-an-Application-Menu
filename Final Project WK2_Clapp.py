# Final Project WK2
from datetime import datetime

print("miccla8284 Spreadsheet Automation Menu.")

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
    print("You selected option:", user_choice, "at", str(datetime.now()))
else:
    print("Error: Invalid choice selected")
