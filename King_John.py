import csv


dictionary =open('King_john.txt')
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

file_out = open("King_John.csv", "w")

''''''
for key, value in counts.items():
    print(key + ','  + str(value) )
    #if value > 20:
     #   print(key + ',' + str(value))
      #  file_out.write(key + "," + str(value) + "\n")
''''''

file_out.close()

