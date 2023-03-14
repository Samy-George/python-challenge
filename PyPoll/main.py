import csv
import os

# Set path for file
csvpath= os.path.join("resources", "election_data.csv")
Candidate = []
Candidate1 ="Charles Casper Stockham"
Candidate2 ="Diana DeGette"
Candidate3 ="Raymon Anthony Doane"
Candidate1_list = []
Candidate2_list = []
Candidate3_list = []
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)

     # Read the header row first
    csv_header = next(csvreader)
    #first_row = next(csvreader)
   # Candidate.append(csv_header[2])
    
    for row in csvreader:
        Candidate.append(row[2])
    

        if row[2] == Candidate1:
            Candidate1_list.append(row[2])

        if row[2] == Candidate2:
            Candidate2_list.append(row[2])

        if row[2] == Candidate3:
            Candidate3_list.append(row[2])

    

can1_votes = str(len(Candidate1_list))
can2_votes = str(len(Candidate2_list))
can3_votes = str(len(Candidate3_list))
total_votes = str(len(Candidate))

# Determine percentage of votes each candidate won
percent1 = round(int(float(can1_votes)) / int(float(total_votes)) * 100, 3)
percent2 = round(int(float(can2_votes)) / int(float(total_votes)) * 100, 3)
percent3 = round(int(float(can3_votes)) / int(float(total_votes)) * 100, 3)       

print("Election Results")   

print(total_votes)

print( str(Candidate1) + " : " + str(percent1) + "%" + "   (" + can1_votes + ")")
print( str(Candidate2) + " : " + str(percent2) + "%" + "   (" + can2_votes + ")")
print( str(Candidate3) + " : " + str(percent3) + "%" + "   (" + can3_votes + ")")

print( "Winner : " + Candidate2)

output_file =  os.path.join("analysis", "analysis.txt")
with open(output_file,"w") as datafile:
    datafile.write("Election Results")
    datafile.write("\n------------------------------------------------")
    datafile.write("\nTotal Votes: " + total_votes)
    datafile.write("\n------------------------------------------------")
    datafile.write("\n"+ str(Candidate1) + " : " + str(percent1) + "%" + "   (" + can1_votes + ")" )
    datafile.write("\n"+ str(Candidate2) + " : " + str(percent2) + "%" + "   (" + can2_votes + ")" )
    datafile.write("\n"+ str(Candidate3) + " : " + str(percent3) + "%" + "   (" + can3_votes + ")" )
    datafile.write("\n------------------------------------------------")
    datafile.write("\nWinner: " + Candidate1)
    datafile.write("\n------------------------------------------------")