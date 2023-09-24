# Import required modules/packages
import os
import csv
import operator

# Store the file path associated with the file
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the file "read mode" and store contents in the variable
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter =',')
    next(csvreader)

    candidatevote  = []       #List of column 2
    candidatelist  = []       #List of candidates participating in election
   
    for row in csvreader:
        
        candidatevote.append(str(row[2]))
        
        if row[2] not in candidatelist:
            candidatelist.append(str(row[2]))
   
print("Election Results")
print("-"*100)
print("Total Votes Casted :", len(candidatevote))
print("-"*100)
print("List of Candidates :", candidatelist)
print("-"*100)

#List of votes won by each candidate
votelist = []
for j in range(len(candidatelist)):
    val1       = candidatelist[j]
    #print(val1)
    count      = operator.countOf(candidatevote,val1)
    percentage = (count/len(candidatevote))*100
    votelist.append(count)
    print("Candidate's Name : "+ str(val1) + ", Votes won : " + str(count) + ", Percentage votes : " + str(percentage) + "%")

print("-"*100)

winner = votelist.index(max(votelist))
#print(winner)
print("Winner is ", candidatelist[winner])

