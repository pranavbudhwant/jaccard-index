# Computing similarity of strings based on jaccard index
Python script to measure the similarity of given address with the addresses in the database based on the jaccard index.
The the script gives best matched addresses in the database to the given address by the user.

Jaccard Index - The Jaccard index, also known as Intersection over Union and the Jaccard similarity coefficient (originally coined coefficient de communauté by Paul Jaccard), is a statistic used for comparing the similarity and diversity of sample sets. The Jaccard coefficient measures similarity between finite sample sets, and is defined as the size of the intersection divided by the size of the union of the sample sets.

File Descriptions:

data.csv:
This file contains the database.
First column specifies the name of the person.
Second column specifies the address of the person.

stopWords.txt:
This file contains the stop words based on the current database. Stop words are words which are filtered out before or after processing of natural language data (text). 
As the jaccard index is based on the number of matching words in two sets, the presence of these words will give us inaccurate results, hence must be removed before processing.
You will have to modify this file and add the stop words based on your database.

cleanString.py:
Python script file containg clean() function, which removes all the stopwords, any redundant characters from a given string.

jaccardIndex.py:
Python script file, accepts the address from the user and calculates the jaccard index for every record in the data.csv file, and sorts the results based on the similarity index and displays the best matched Name-Address tuples.
