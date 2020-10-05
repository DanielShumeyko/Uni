import numpy as np
import re

#Parse word list from file
file_location = str(input('Input file location:')) # C:\\Users\\Daniel\\Desktop\\Uni\\Lang\\Lab1\\test.txt
input_file = open(file_location, 'r').read() 
delims = ',|\.|:|\n|;|\*|\+|\-|\?|\!|\(|\)|\=|\s+'
words = re.split(delims, input_file)

#Trim empty strings and shorten words to their limit of 30 characters
for i, word in enumerate(words):
    if word is '' or word is ' ':
        words.remove(word)
    if len(word) > 30:
        words[i] = word[:30]

#Initiating the distance matrix
n = len(words)
distances = np.zeros((n,n), dtype=int)

#Creating function for calculating distance between 2 words
#note that if one word is n letters longer it is trimmed by those n letters and distance increases by n
def dist(a,b):
    distance = 0
    word1 = a
    word2 = b
    len1 = len(word1)
    len2 = len(word2)
    if len1 > len2:
        distance += len1 - len2
        word1 = word1[:len2]
    elif len1 < len2:
        distance += len2 - len1
        word2 = word2[:len1]

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1
    return distance

for i in range(len(words)):
    for j in range(len(words)):
        distances[i,j] = dist(words[i], words[j])

#Find the maximum distance(s) and get their indexes in a list of pairs
max_dist = np.amax(distances)
max_coords = tuple(zip(*np.where(distances==max_dist)))

#Here we need to remove reversed dupliicates from out list, example: [0, 1] and [1, 0]
#In order to do this we sort each pair and conver the paiirs to tuples. Then we convert the list of tuples to a set to eliminate repeats. Finally, we convert it back to a list.
max_distances = [list(tpl) for tpl in list(set([tuple(sorted(pair)) for pair in max_coords]))]

#Here we put the maximum distance and all pairs of words with this distance into a string and display it
output = "\n\nThe longest distance between two words is " + str(max_dist) + ". \nThe pairs of words with the maximum distance are:\n"
for pair in max_distances:
    output += words[pair[0]] + " and " + words[pair[1]] + "\n"
print(output)