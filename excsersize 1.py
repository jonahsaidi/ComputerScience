
fhand = open("exersize.txt", 'r') #opens file 
email_addresses = {} #create dictionary 

for line in fhand: #for loop and "in" is checking if the object is inside the list 
    if line.startswith("From "): #if the line starts with "from"(pretty literal code there)
        email = line.split()[1]#get it at the 1th location 
        email_addresses[email] = email_addresses.get(email, 0) + 1 #add one to it if its there, otherwise its 1

lst = [] #creates list 
for key, value in email_addresses.items():
    lst.append((value,key))

lst.sort(reverse=True)
person_tuple = lst[0]
print(person_tuple[1], person_tuple[0])