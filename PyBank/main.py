#pybank main
import os
import csv

csvpath = os.path.join('Desktop', 'budget_data.csv')

# Variables 
month = []
revenue = []
previous_revenue = 0   
max_increase = 0
max_decrease = 0

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first 
    csv_header = next(csvreader)

    # Month and Revenue
    for row in csvreader:
        month.append(row[0])
        revenue.append(int(row[1]))

total_revenue = sum(revenue)          
previous_revenue = 0     
change_list = []  

for i in range(len(revenue)):
    change = (revenue[i]) - previous_revenue
    change_list.append(change)
    previous_revenue = revenue[i]
  
# Average Change
average_change = sum(change_list[1:86]) / (len(month) -1)  

# Greatest Increase
greatest_increase = max(change_list[1:86])
greatest_increase_index = (change_list.index(max(change_list[1:86])))
max_increase_date = month[greatest_increase_index]

#Greatest Decrease
greatest_decrease = min(change_list[1:86])
greatest_decrease_index = (change_list.index(min(change_list[1:86])))
max_decrease_date = month[greatest_decrease_index]

#PyBank Analysis   
print("Financial Analysis")
print("--------------------------")     
print("Total Months: " + str(len(month)))
print("Total Revenue: $" + str(total_revenue))
print("Average Change: $" + str(round(average_change,2)))
print("Greatest Increase in Profits: " + max_increase_date + " $" + str(greatest_increase))
print("Greatest Decrease in Profits: " + max_decrease_date + " $" + str(greatest_decrease))

#Export a text file with the results.
fileoutput = os.path.join("PyBankAnalysis.txt")
with open(fileoutput, 'w', newline="") as textfile:
    textfile.write("Financial Analysis" + "\n")
    textfile.write("------------------------- " + "\n")
    textfile.write("Total Months: " + str(len(month)) +"\n")
    textfile.write("Total Revenue: $" + str(total_revenue) +"\n") 
    textfile.write("Average Change: $" + str(round(average_change,2)) +"\n")
    textfile.write("Greatest Increase in Profits: " + max_increase_date + " $" + str(greatest_increase) +"\n")
    textfile.write("Greatest Decrease in Profits: " + max_decrease_date + " $" + str(greatest_decrease) +"\n") 
  
#Print the analysis to the terminal.
with open (fileoutput, 'r', newline='') as terminalprint:
    printtoterminal=terminalprint.read()
    print(printtoterminal)