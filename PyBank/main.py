import os
import csv
import sys

csvfile1 = os.path.join("../","PyBank","budget_data_1.csv")

csvfile2 = os.path.join("../","PyBank","budget_data_2.csv")

# Read the csv and convert it into a list of dictionaries
with open(csvfile1) as revenue_analysis_1:
    reader = csv.reader(revenue_analysis_1)

    # use of next to skip first title row in csv file
    next(reader) 
    revenue = []
    count = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in reader:

        revenue.append(float(row[1]))
        count.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(count))
    print("Total Revenue: $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(count[rev_change.index(max(rev_change))])
        min_rev_change_date = str(count[rev_change.index(min(rev_change))])


    print("Avereage Revenue Change: $",avg_rev_change)
    print("Greatest Increase in Revenue:", max_rev_change_date,"($",max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($",min_rev_change,")")




#         count += 1
#         total += int(row[1])

# print("Total months:  " +str(count))
# print ("Total Revenue: $" +str(total))


# Revenue = data_file ["Revenue"]
# change_list = [0]
# for index, element in enumerate(Revenue):
#   current_value = element
#   next_value = Revenue[(index + 1)% len(Revenue)]
#   difference = current_value - next_value
# change_list.append(difference)

# a = sum(change_list) 
# a


# def extract_column_data(list_of_paths, column_name):

#     #container for data extracted from each csv file
#     column_data = []
#     #loop through list of csv files
#     for x in list_of_paths:

#         #opens csv as a dictreader object and assigns it to variable data_dict
#         data_dict= csv.DictReader(open(list_of_paths[x]))
#         #loop through data and put values into the list defined above
#         for row in data_dict:
#             column_data.append(row[column_name])
#     return column_data




# # with open("file.csv") as fin:
# # with open(csvfile1, 'r') as fin:
# #     headers = next(count_file)
# #     total = 0
# #    for row in csv.reader(count_file):
# #         total += int(row[1])
# # print (total)
# # print (headers)

# # with open(csvfile2, newline="") as csvfile22:
# # 	csvreader2 = csv.reader(csvfile22,delimiter = ",")

	


# 	