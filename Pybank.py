import csv
budget = "C:/Users/jessi/KUBootCamp/ku-edw-data-pt-07-2020-u-c/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"
#print (budget)
with open (budget, "r", encoding="utf-8") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")
    next (csvreader)
    total_months = []
    total_pl = []
    pl_change = []
    for row in csvreader:
        total_months.append(row[0])
        total_pl.append(int(row[1]))
    Total_Months = len(total_months)
    Total_ProfitLoss = sum(total_pl)
    for i in range(1,len(total_pl)):
        pl_change.append(int(total_pl[i])-int(total_pl[i-1]))
    average_change = sum(pl_change)/len(pl_change)
    greatestincrease = max(pl_change)
    date_max= total_months[pl_change.index(greatestincrease)+1]
    greatdecrease = min(pl_change)
    datemin = total_months[pl_change.index(greatdecrease)+1]
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {Total_Months}")
    print(Total_ProfitLoss)
    print(average_change)
    print(greatestincrease)
    print(greatdecrease)
    print(datemin)
anylt_spot = "C:/Users/jessi/KUBootCamp/ku-edw-data-pt-07-2020-u-c/02-Homework/03-Python/Instructions/PyBank/anaylsis/fanancialresere.txt"
with open (anylt_spot, 'w') as writecsv:
    writecsv. write("Financial Analysis")
    writecsv.write("---------------------------------")
    writecsv.write(f"Total Months: {Total_Months}")
    writecsv.write(f"nettotalprofitloss: ${Total_ProfitLoss}")
    writecsv.write(f"avgpoftlos: ${average_change}")
    writecsv.write(f"grt: ${greatestincrease} {date_max}")
    writecsv.write(f"GD: ${greatdecrease} {datemin}")
    #ritecsv.writedatemin
    