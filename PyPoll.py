#PyPoll HomeWork
path = "C:/Users/jessi/ku-edw-data-pt-07-2020-u-c/02-Homework/03-Python/Instructions/PyPoll/Resources"
electionData = 
print(Election Results)
print(-----------------------------)

with open (electionData"r", encoding="utf-8") as csvfile:
    cvsreader = cvs.reader(cvsfile, delimiter = ",")
  
  
    next (cvsreader)
    total_votes_cast = []
    
    candidate_votes = []
    percentage_votes_won = []
    popular_vote_winner = []