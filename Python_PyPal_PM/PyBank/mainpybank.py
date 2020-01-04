# Module for reading CSV files
import csv
#input_file
csvpath = "Resources/budget_data.csv"

# Creating empty lists to iterate through the rows and get total values
months = []
total_amount = []

# Reading of CSV file

with open(csvpath, newline='') as csvfile:

    # Store the contents of budget_data.csv in the variable csvreader and convert to list
    csvreader = csv.reader(csvfile, delimiter=',')
    csvlist= list(csvreader)[1 :]
    
    # Reading each row of data in the list
    for row in csvlist:
        months.append(row[0])
        total_amount.append(int(row[1]))
        
    #defining empty list to store net change and compute the values
    net_change = []

    for i in range(len(total_amount)-1):
        net_change.append(total_amount[i+1] - total_amount[i])
    sum_netchange = sum(net_change)
    average_change = sum_netchange/(int(len(months))-1)
    
#calculating max and min changes in profits
    max_index = net_change.index(max(net_change))
    min_index = net_change.index(min(net_change))

#print analysis to terminal
    print("Financial Analysis")
    print("-------------------------")
    print(f'Total Months: {len(months)}')
    print(f'Total: ${sum(total_amount)}')
    print(f'Average Change: ${round((average_change),2)}')
    print(f'Greatest Increase in Profits: {months[max_index+1]} (${net_change[max_index]})')
    print(f'Greatest Decrease in Profits: {months[min_index+1]} (${net_change[min_index]})')

#output_file
txtpath = "Output/budget_data.txt"

#export analysis to text file
with open(txtpath, "w") as output_file:
    output_file.write("Financial Analysis")
    output_file.write("\n")
    output_file.write("----------------------")
    output_file.write("\n")
    output_file.write(f'Total Months: {len(months)}')
    output_file.write("\n")
    output_file.write(f'Total: ${sum(total_amount)}')
    output_file.write("\n")
    output_file.write(f'Average Change: ${round((average_change),2)}')
    output_file.write("\n")
    output_file.write(f'Greatest Increase in Profits: {months[max_index+1]} (${net_change[max_index]})')
    output_file.write("\n")
    output_file.write(f'Greatest Decrease in Profits: {months[min_index+1]} (${net_change[min_index]})')
