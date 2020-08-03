##################################################
## Author: MK3K 
## Date: 20200801
## This code makes democracy function as intended  
##################################################

# imports the necessary libraries needed to manipulate csv files 

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the data file.
#election_data = open('election_results-topdirectory.csv','r')

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # This provided this type of output: 
    #print(election_data)

    # reads in tabular data via the reader function
    file_reader = csv.reader(election_data)

    # Prints entire table 
    #for row in file_reader:
            #print(row)

    #prints the table headings: ['Ballot ID', 'County', 'Candidate']
    headers = next(file_reader)
    #print(headers)


    #Add a vote count for each candidate.
    total_votes = 0 
    candidate_options=[]
    candidate_votes = {}
    # Track the winning candidate, vote count, and percentage.
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    for row in file_reader:
        total_votes += 1
        #Write down the names of all the candidates.

        # Get the candidate name from each row.
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #adds new value to candidate_options[]
            candidate_options.append(candidate_name)
            #Begin tracking new candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    with open(file_to_save, "w") as txt_file:
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        #print output        
        #print(f"the total number of votes cast is {total_votes:,}")

        #print(candidate_options)

        #print(candidate_votes)

        for candidate_name in candidate_votes:
            # Retrieve vote count and percentage.
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print each candidate, their voter count, and percentage to the
            # terminal.
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage
        # Print the winning candidates' results to the terminal.
        election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                )
        print(election_results, end="")

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

    #election_data.close()