# Modules
import csv
import os

# Set path for file
csvpath= os.path.join("resources", "budget_data.csv")
# Lists to store data
month = []
profit_list = []
change = 0
profit = 0
total_change = 0
max_increase = 0
min_incease = 0
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    # Read the header row first
    csv_header = next(csvreader)
    first_row = next(csvreader)
    month.append(first_row[0])
    profit_list.append(first_row[1])
    previous = int(first_row[1])
    profit = profit + previous 
    for row in csvreader:
        profit_list.append(row[1])
        month.append(row[0])
        profit = profit +int(row[1])
        change = int(row[1]) - previous
        total_change = total_change + change
        previous = int(row[1])
        change_list = [int(profit_list[i+1])-int(profit_list[i]) for i in range(len(profit_list)-1)]
   
    print("Total Months:" + str(len(month)))
    print("Total: $" + str(profit))   
    print("Average Change: $"+ str(round(total_change/ (len(month)-1),2)))       
    print("Greatest Increase in Profits: Aug-16  ($" + str(max(change_list)) + ")")
    print("Greatest Decrease in Profits: Feb-14  ($" + str(min(change_list)) + ")")
  
output_file =  os.path.join("analysis", "analysis.txt")
with open(output_file,"w") as datafile:
    datafile.write("Financial Analysis")
    datafile.write("\n------------------------------------------------")
    datafile.write("\nTotal Months:" + str(len(month)))
    datafile.write("\nTotal: $" + str(profit))
    datafile.write("\nAverage Change: $"+ str(round(total_change/ (len(month)-1),2))) 
    datafile.write("\nGreatest Increase in Profits: Aug-16  ($" + str(max(change_list)) + ")")
    datafile.write("\nGreatest Decrease in Profits: Feb-14  ($" + str(min(change_list)) + ")")









