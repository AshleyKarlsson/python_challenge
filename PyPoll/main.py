#pypoll main
import os
import csv

csvpath = os.path.join('Desktop', 'election_data.csv')

#Variables
voter_id = []
candidate = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

  # Read each row of data after the header
    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])

#A complete list of candidates who received votes
unique = set(candidate)
candidate_list = list(unique)

#The total number of votes each candidate won
candidate_zero_votes = candidate.count(candidate_list[0])
candidate_one_votes = candidate.count(candidate_list[1])
candidate_two_votes = candidate.count(candidate_list[2])
candidate_three_votes = candidate.count(candidate_list[3])

#The percentage of votes each candidate won
candidate_zero_percentage = candidate_zero_votes / len(voter_id)*100
candidate_one_percentage = candidate_one_votes / len(voter_id)*100
candidate_two_percentage = candidate_two_votes / len(voter_id)*100
candidate_three_percentage = candidate_three_votes / len(voter_id)*100

#The winner of the election based on popular vote.
election = [candidate_zero_votes, 
            candidate_one_votes, 
            candidate_two_votes, 
            candidate_three_votes
            ]
election_results = sorted(election)
winner = election.index(election_results[-1])

#Election Results Analysis
print("Election Results")
print("-------------------------")
print("Total Votes:  " + str(len(voter_id)))
print("-------------------------")
print((candidate_list[0]) +" "+ str(round(candidate_zero_percentage,3)) + "% " + str(candidate_zero_votes))
print((candidate_list[1]) +" "+ str(round(candidate_one_percentage,3)) + "% " + str(candidate_one_votes))
print((candidate_list[2]) +" "+ str(round(candidate_two_percentage,3)) + "% " + str(candidate_two_votes))
print((candidate_list[3]) +" "+ str(round(candidate_three_percentage,3)) + "% " + str(candidate_three_votes))
print("-------------------------")
print("Winner: " + candidate_list[winner])
print("-------------------------")

#Export a text file with the results.
fileoutput = os.path.join("ElectionResultsAnalysis.txt")
with open(fileoutput, 'w', newline="") as textfile:
    textfile.write("Election Results ")
    textfile.write("\n------------------------- ")
    textfile.write("\nTotal Votes:  " + str(len(voter_id)) +"\n")
    textfile.write((candidate_list[0]) +" "+ str(round(candidate_zero_percentage,3)) + "% " + str(candidate_zero_votes) +"\n") 
    textfile.write((candidate_list[1]) +" "+ str(round(candidate_one_percentage,3)) + "% " + str(candidate_one_votes) +"\n")
    textfile.write((candidate_list[2]) +" "+ str(round(candidate_two_percentage,3)) + "% " + str(candidate_two_votes) +"\n")
    textfile.write((candidate_list[3]) +" "+ str(round(candidate_three_percentage,3)) + "% " + str(candidate_three_votes) +"\n")
    textfile.write("\n-------------------------")
    textfile.write("\nWinner: " + candidate_list[winner])
    textfile.write("\n-------------------------")  
  
#Print the analysis to the terminal.
with open (fileoutput, 'r', newline='') as terminalprint:
    printtoterminal=terminalprint.read()
    print(printtoterminal)