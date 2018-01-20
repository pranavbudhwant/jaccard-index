import csv
import re
import operator

address = input("Enter address: ")

stop_words = []
sortedMatches = []

#stopWords.txt --> contains the manually added stopwords(each on a newline).
with open('stopWords.txt','r') as stopWordFile:
	tWord = stopWordFile.readline()
	tWord = tWord.strip('\n')
	stop_words.append(tWord)
	while tWord:
		tWord = stopWordFile.readline()
		tWord = tWord.strip('\n')
		if tWord not in stop_words: #Avoid duplicates
			stop_words.append(tWord)


#This function accepts two lists as parameters and returns the jaccard index.
def jaccardIndex(x,y):
	intersection = len(list(set(x).intersection((set(y)))))
	union = len(list(set(x).union((set(y)))))
	return intersection/union


#This function accepts a string as parameter and returns a "clean" string.
#Redundant words,characters are removed from the string using regular expressions
#(based on the current dataset, you will have to modify this function for your dataset).
def cleanString(temp):
	temp = temp.lower()

	#Remove special characters:
	temp = re.sub(r'\b\\\b|\b\/\b|\b\\\b|\.|\@|[A-Za-z][A-Za-z]\d{1,3}|\:|\#|\&|\'|\;|\-','',temp)

	#Replace + with '(space)'
	temp = re.sub(r'\b\+\b',' ',temp)

	#Remove all redundant groups of characters:
	temp = re.sub(r'(\b\d{1,3}\b|\b[A-Za-z]{3}\b|\b[A-Za-z]{2}\b|\ [A-Za-z]\ |\b[A-Za-z]+\/[A-Za-z]+\b|\b\d{1,2}[A-Za-z]+\b|\.)','',temp)
	#1-3 digit number|3 characters|2 characters|(space)single character(space)|character(s)/character(s)|1-2 digits followed by character(s)|.

	#Repeat removal
	temp = re.sub(r'\b\\\b|\b\/\b|\b\\\b|\.|\@|[A-Za-z][A-Za-z]\d{1,3}|\:|\#|\&|\'','',temp)
	temp = re.sub(r'\(|\)',' ',temp)
	temp = re.sub(r'(\b\d{1,3}\b|\b[A-Za-z]{3}\b|\b[A-Za-z]{2}\b|\ [A-Za-z]\ |\b[A-Za-z]+\/[A-Za-z]+\b|\b\d{1,2}[A-Za-z]+\b|\.)','',temp)

	temp = re.sub(r'\b[A-Za-z]\b','',temp)

	#Remove all the stop words from the current string.
	queryWords = temp.split()
	resultWords = [word for word in queryWords if word.lower() not in stop_words]
	result = ' '.join(resultWords)

	return result

with open('data.csv') as dataFile:
	data = csv.reader(dataFile)

	address = cleanString(address)
	x = re.split('; |, | |- |,|;|-|\.',address) #Create a list of words from the string, separated by any special character.
	for row in data:
		adr = row[1]
		adr = cleanString(adr)
		y = re.split('; |, | |- |,|;|-|\.',adr) #Create a list of words from the string, separated by any special character.

		si = jaccardIndex(x,y)
		sortedMatches.append((row[0],row[1],si))

sortedMatches.sort(key=operator.itemgetter(2)) #Sort the records based on the similarity index/jaccard index.

#Sort gives us ascending order, for descending order:
sortedMatches.reverse()

#Prints the matching data found based on a threshold, alternatively you can print all the records.
print("\nBest Found Matches: ")
for record in sortedMatches:
	if record[2]>=0.2: #You can modify the threshold, depending on the required sensitivity.
		print(record)