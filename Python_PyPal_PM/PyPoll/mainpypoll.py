# Module for reading CSV files
import csv
#input_file
csv_path = ("Resources/election_data.csv")
#output_file
txt_path = ("Output/election_data.txt")

# Creating empty lists to iterate through the rows and get total values
total_votes = []
list_candidates = []

# Reading of CSV file
with open (csv_path, newline='') as csvfile:
    
    # Store the contents of election_data.csv in the variable csvreader and convert to list
    csvreader = csv.reader(csvfile, delimiter=',')
    csvlist = list(csvreader)[1 :]

    for row in csvlist:
        total_votes.append(row[0])
        list_candidates.append(row[2])
    
    #get a unique list of values from the list_candidates above using set and conver the set to list
    unique_setcandidates = set(list_candidates)
    unique_listcandidates = list(unique_setcandidates)

    votecount=[]
    for name in unique_listcandidates:
        count = 0
        for row in csvlist:
            if name==row[2]:
                count+=1
        votecount.append(count)

percentagevote =[]
for item in votecount:
    percentagevote.append((item/len(total_votes) * 100))
Roundedpercentagevote = ["%.3f"%item for item in percentagevote]

#finding the index of the max vote count from the list of votecount to identify the winner
max_index = votecount.index(max(votecount))
winner = unique_listcandidates[max_index]

#print analysis to terminal and output file
with open(txt_path, "w") as output_file:
    print("Election Results")
    output_file.write("Election Results")
    output_file.write("\n")
    print("-------------------------")
    output_file.write("----------------------")
    output_file.write("\n")
    print(f'Total Votes: {len(total_votes)}') 
    output_file.write(f'Total Votes: {len(total_votes)}')
    output_file.write("\n")
    print("-------------------------")
    output_file.write("----------------------")
    output_file.write("\n")
    #printing the list of candidates and percentage votes and votecount in order of highest to lowest votes
    finalcandidate = ''
    finalpercentage = 0.000
    finalvotecount = 0
    for i in range(len(votecount)):
        indexofmax = votecount.index(max(votecount))
        finalcandidate = unique_listcandidates[indexofmax]
        finalpercentage = Roundedpercentagevote[indexofmax]
        finalvotecount = votecount[indexofmax]
        print("{}: {}% ({})".format(finalcandidate, finalpercentage, finalvotecount))
        output_file.write("{}: {}% ({})".format(finalcandidate, finalpercentage, finalvotecount))
        output_file.write("\n")
        unique_listcandidates.pop(indexofmax)
        votecount.pop(indexofmax)
        Roundedpercentagevote.pop(indexofmax)
    print("-------------------------")
    output_file.write("-------------------------")
    output_file.write("\n")
    print(f'Winner: {winner}')
    output_file.write(f'Winner: {winner}')
    output_file.write("\n")
    print("-------------------------")
    output_file.write("-------------------------")
    

