#create program across operating systems
import os 
#reads csv files
import csv

file_to_load = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#file_to_load = os.path.join('PyBank', 'Resources', 'budget_v4.csv')
file_to_output = os.path.join('PyBank', 'Analysis', 'budget_analysis.txt')
#initializing variables 
total_months = 0
prev_revenue = 0
total_revenue = 0
months_of_change = []
revenue_change_list = []
#"" placeholder - range
#Comparing the number to 0 and 99999999
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999]

#revenue_data is a variable that holds content
with open(file_to_load) as revenue_data:
    #each column separated by a comma
    csvreader = csv.reader(revenue_data, delimiter = ',')
    #reader = csv.DictReader(revenue_data)
    print (csvreader)
    #header
    csv_header = next(csvreader)


    for row in csvreader:
        #adding months together 
        total_months += 1
        total_revenue += int(row[1])

        #print(total_revenue)
        print(" ")
        print(prev_revenue)
        print(int(row[1]))
    

        revenue_change = int(row[1]) - prev_revenue
        print(revenue_change)
        prev_revenue = int(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        #print(revenue_change_list)
        months_of_change = months_of_change + [row[0]]
        #print(months_of_change)

        #print(revenue_change)
        #print(greatest_increase[1])
        #Loops through all the profit/loss and compares it with initial value to find greatest_increase & greatest_decrease
        if revenue_change > greatest_increase[1]:
            #print("Yes", row[0])
            #print(" ")
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change

        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change
        #FIX
    #revenue_avg = total_revenue/ (total_months)
    revenue_avg = sum(revenue_change_list)/len(revenue_change_list)
    print(" ")
    #print(total_revenue)
    #print(total_months)


output=(
   f"\nFinancial Analysis\n"
    f"====================\n"
    f"Total Months:  {total_months}\n"
    f"Total: ${total_revenue}\n"
    f"Average Change: ${revenue_avg}\n"
    f"Greatest Increase in Profits : {greatest_increase}\n"
    f"Greatest Decrease in Profits : {greatest_decrease}\n"
)
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


