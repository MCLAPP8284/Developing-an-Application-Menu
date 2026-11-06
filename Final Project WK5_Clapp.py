# Final Project WK5 - Geraphing Dynamically Generated Data
from datetime import datetime
import openpyxl
from openpyxl.chart import BarChart, LineChart, Reference

print("miccla8284 Spreadsheet Automation Menu.")

#Write the data to a CSV file
def insertData(filePath, data):
    try:
        file = open(filePath, "a")
        file.write(data + "\n")
        file.close()
    except:
        print("Error writing to file")

#Show CSV contents
def viewData(filePath):
    try:
        print("Reading from:", filePath)
        file = open(filePath, "r")
        for line in file:
            print(line.strip())
        file.close()
    except:
        print("Error reading file")

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

        data = date + "," + str(value) + "," + str(convertedValue)
        try:
            insertData("ZooData.csv", data)
            print("The following data was saved at", datetime.now(), ":", data)
        except:
            print("Error saving data")

#Create the excel chart from the CSV data- CSV file path and chart type
def createChart(filePath, chartType):
    wb = openpyxl.Workbook()
    ws = wb.active
    print("Selected Data Source")
    print("1. Fahrenheit")
    print("2. Celsius")

    dataSource = input()
    ws["A1"] = "Date"
    ws["B1"] = "Temperature"
    try:
        file = open(filePath, "r")
        row = 2
        for line in file:
            values = line.strip().split(",")
            ws.cell(row=row, column=1).value = values[0]
            if dataSource == "1":
                ws.cell(row=row, column=2).value = float(values[1])
            else:
                ws.cell(row=row, column=2).value = float(values[2])
            row += 1
        file.close()

        data = Reference(ws, min_col=2, min_row=1, max_row=row - 1)
        labels = Reference(ws, min_col=1, min_row=2, max_row=row - 1)
        if chartType == "bar":
            chart = BarChart()
        else:
            chart = LineChart()

        chart.title = "Temperature Log"
        chart.x_axis.title = "Date"
        chart.y_axis.title = "Temperature"

        chart.add_data(data, titles_from_data=True)
        chart.set_categories(labels)

        ws.add_chart(chart, "D2")
        wb.save("final.xlsx")

        print("Report saved as final.xlsx")
    except Exception as e:
        print("Error creating report")
        print(e)

#Create report and select chart type- CSV file path
def generateReport(filePath):
    print("Select Chart Type")
    print("1. Bar Chart")
    print("2. Line Chart")

    chartChoice = input()
    if chartChoice == "1":
        createChart(filePath, "bar")
    elif chartChoice == "2":
        createChart(filePath, "line")
    else:
        print("Invalid selection")
        
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
    elif user_choice == "2":
        viewData("ZooData.csv")
    elif user_choice == "3":
        generateReport("ZooData.csv")
    else:
        print("Error: Invalid choice selected")
