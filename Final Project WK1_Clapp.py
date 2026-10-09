# Final Project
from datetime import datetime

print("miccla8284 Spreadsheet Automation Menu.")

# Required Menu options
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stors into the variable called user_choice
user_choice = input()

# Output shows selected option, date and date
print("You selected option:", user_choice, "at", str(datetime.now()))
