# imports the necessary libraries needed to manipulate csv files 

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Prints entire csv table -- do not uncomment or else run time will murder you
    #for row in file_reader:
            #print(row)

    #skips the headers in the csv table
    headers = next(file_reader)
    #prints the table headings: ['Ballot ID', 'County', 'Candidate']
    #print(headers)

    #Add a vote count for each candidate.
    total_votes = 0 
    candidate_options = []
    candidate_votes = {}
    # Track the winning candidate, vote count, and percentage.
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    # Track a vote count for each county.
    voter_turnout = 0     
    county_options = []
    county_turnout = {}
    # Track the county with the highest vote count and percentage
    highest_turnout = ""
    winning_county = "" 
    winning_county_count = 0
    winning_county_percentage = 0 

    for row in file_reader:
        total_votes += 1 #sums all the rows, ie. votes cast
        # Get the candidate name from each row.
        candidate_name = row[2] #reference header printout above for row contents
        if candidate_name not in candidate_options:
            #adds new value to candidate_options[]
            candidate_options.append(candidate_name)
            #Begin tracking new candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        highest_turnout = row[1] #reference header printout above for row contents
        if highest_turnout not in county_options:
            #adds new value to county_options[]
            county_options.append(highest_turnout)
            #Begin tracking new county's vote count
            county_turnout[highest_turnout] = 0
        # Add a vote to that county's count
        county_turnout[highest_turnout] += 1

    #writes to text file. 
    with open(file_to_save, "w") as txt_file:
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)


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
        
        ###Prints with the following formatting:
        #-------------------------
        #Winner: X
        #Winning Vote Count: X
        #Winning Percentage: X
        #-------------------------
        ###

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

    #COUNTETY COUNT FOR THE ROYAL COUNTED POLICE
        for highest_turnout in county_turnout:
            # Retrieve vote count and percentage.
            county_votes = county_turnout[highest_turnout]
            county_vote_percentage = float(county_votes) / float(total_votes) * 100
            # Print each candidate, their voter count, and percentage to the
            # terminal.
            print(f"{highest_turnout}: {county_vote_percentage:.1f}% ({county_votes:,})\n")
            county_results = (f"{highest_turnout}: {county_vote_percentage:.1f}% ({county_votes:,})\n")
            txt_file.write(county_results)

            if (county_votes > winning_county_count) and (county_vote_percentage > winning_county_percentage):
                winning_county_count = county_votes
                winning_county = highest_turnout
                winning_county_percentage = county_vote_percentage

        winning_county_summary = (
            f"-------------------------\n"
            f"County with Highest Turnout: {winning_county}\n"
            f"Voter Turnout: {winning_county_count:,}\n"
            f"Percentage of Total Voters: {winning_county_percentage:.1f}%\n"
            f"-------------------------\n")

        print(winning_county_summary)
        txt_file.write(winning_county_summary)
