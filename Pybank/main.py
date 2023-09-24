# Import required modules/packages
import os
import csv
import operator

# Store the file path associated with the file
csvpath = os.path.join('Resources','budget_data.csv')

# Open the file "read mode" and store contents in the variable
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter =',')
    # use of next to skip first title row in csv file
    next(csvreader)

    #Define empty lists for revenue-profit/loss and Totalmonths-number of months
    revenue     = []
    Totalmonths = []

    #Make a list of column 0 and 1 from csv file using for loop
    for row in csvreader:

        Totalmonths.append(row[0])     #List of column 0
        revenue.append(float(row[1]))  #List of column 1

    print("Financial Analysis")
    print("-"*100)
    print("Total Months : ", len(Totalmonths))
    print("-"*100)
    print("Total : $", sum(revenue))
    print("-"*100)
 
    #Define empty list of revenue-profit/loss as change
    change      = []
    for i in range(1,len(revenue)):
        change.append(revenue[i] - revenue[i-1])
        
    #Calculate average profit/loss, maxamium and minimum change
    average    = sum(change)/len(change)
    maxchange  = max(change)
    minchange  = min(change)
    imaxchange = change.index(max(change))
    iminchange = change.index(min(change))

    maxdate = Totalmonths[imaxchange]
    mindate = Totalmonths[iminchange]

    print("Avereage Change : $" + str(average))
    print("-"*100)
    print("Greatest Increase in Profits : " + str(maxdate) + " = $" + str(maxchange))
    print("-"*100)
    print("Greatest Decrease in Profits : " + str(mindate) + " = $" + str(minchange))
