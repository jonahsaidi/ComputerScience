import csv


dictionary =open('words.txt')
counts = dict() #counts is the dictionary 
for line in dictionary:
    line = line.upper()
    words = line.split()
    for word in words: 
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)


file_out = open("Romeo_Juliet_output.csv", "w")

for key,value in counts.items():

    if value > 20:
        print(key + ',' + str(value))
        file_out.writelines(key + "," + str(value) + "\n")

file_out.close()

