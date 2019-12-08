#create program across operating systems
import os 
#reads csv files
import csv

file_to_load = os.path.join('PyPoll', 'Resources', 'election_data.csv')
file_to_output = os.path.join('PyPoll', 'Analysis', 'election_analysis.txt')

#initializing variables
total_votes = 0 
#new list with canditates names just one
candidates= []
#original list of canditates names repeated multiple times
candidate_list = []


with open(file_to_load) as election_data:
    #each column separated by a comma
    csvreader = csv.reader(election_data, delimiter = ',')
    #reader = csv.DictReader(revenue_data)
    print (csvreader)
    #header
    csv_header = next(csvreader)
   #going through rows and reading them
    for row in csvreader:
        #print(row)
        #print(row[2])
        #adding 
        total_votes += 1
       #print (total_votes)
       #add values in column 2 to candidate_list
        candidate_list.append(row[2])
    #print(candidate_list)
#take out items from canditate_list and put them in candidates
for i in candidate_list:
    if i not in candidates:
        candidates.append(i)
#print(candidates)


total0 = candidate_list.count(candidates[0])
#print(total0)
total1 = candidate_list.count(candidates[1])
#print(total1)
total2 = candidate_list.count(candidates[2])
#print(total2)
total3 = candidate_list.count(candidates[3])
#print(total3)
percent0 = (total0/total_votes) * 100
#print (percent0)
percent1 = (total1/total_votes) * 100
#print (percent1)
percent2 = (total2/total_votes) * 100
#print (percent2)
percent3 = (total3/total_votes) * 100
#print (percent3)


dict = {}
dict = {candidates[0]: percent0, candidates[1]: percent1, candidates[2]: percent2, candidates[3]: percent3}
key = ""
count = 0
#print(dict)
for winner in dict:
   if dict[winner] > count:
     key = winner
     count = dict[winner]
#print(key, "", count)
#for item in dict:
    #if item > dict[1]
        #winner = item



#Produces output
output=(
    f"\nElection Results\n"
    f"------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------------\n"
    f"{candidates[0]}: {percent0:.3f}% ({total0})\n"
    f"{candidates[1]}: {percent1:.3f}% ({total1})\n"
    f"{candidates[2]}: {percent2:.3f}% ({total2})\n"
    f"{candidates[3]}: {percent3:.3f}% ({total3})\n"
    f"------------------------\n"
    f"Winner: {key}\n"
    f"------------------------\n"
)
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)