import csv
import re
import operator
import cleanString

address = input("Enter address: ")

sortedMatches = []

#This function accepts two lists as parameters and returns the jaccard index.
def jaccardIndex(x,y):
	intersection = len(list(set(x).intersection((set(y)))))
	union = len(list(set(x).union((set(y)))))
	return intersection/union

with open('data.csv') as dataFile:
	data = csv.reader(dataFile)

	address = cleanString.clean(address)
	x = re.split('; |, | |- |,|;|-|\.',address) #Create a list of words from the string, separated by any special character.
	for row in data:
		adr = row[1]
		adr = cleanString.clean(adr)
		y = re.split('; |, | |- |,|;|-|\.',adr) #Create a list of words from the string, separated by any special character.

		si = jaccardIndex(x,y)
		sortedMatches.append((row[0],row[1],si))

sortedMatches.sort(key=operator.itemgetter(2)) #Sort the records based on the similarity index/jaccard index.

#Sort gives us ascending order, for descending order:
sortedMatches.reverse()

#Prints the matching data found based on a threshold, alternatively you can print all the records.
print("\nBest Found Matches: ")
for record in sortedMatches:
	if record[2]>=0.3: #You can modify the threshold, depending on the required sensitivity.
		print(record)
