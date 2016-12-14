import csv as csv
import numpy as np


csv_file_object = csv.reader(open('train.csv', 'rb')) 


header = csv_file_object.next()

data=[]

for row in csv_file_object:      #Run through each row in the csv file
    data.append(row)             #adding each row to the data variable
data = np.array(data)            #Then convert from a list to an array
			         #Be aware that each item is currently
                                 #a string in this format

#column 0 index(+1)
#column 1 survived/dead 1 for survived
#column 2 Passenger class
#column 3 Name
#column 4 Sex
#column 5 Age
#column 6 #siblings/spouses
#column 7 #parents/children aboard
#column 8 Ticket Number
#column 9 Passenger Fare
#column 10 Cabin
#column 11 Port of Origin (Cherbourg, Queenstown, Southhampton)

number_passengers = np.size(data[0::,0].astype(np.float))
print number_passengers
number_survived = np.sum(data[0::,1].astype(np.float))

print number_survived

percent_survived = number_survived/number_passengers

print percent_survived

women_only_stats = data[0::,3] == "female"
men_only_stats = data[0::,3] != "female"
