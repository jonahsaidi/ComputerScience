alphabet = 'abcdefghijklmnopqrstuvxwyz' #the alphabet 

fhand = open("exersize.txt", 'r') #opens the file 
text = fhand.read() #reads the file 

freq_dict = {} #creates dictionary 
for ch in text.lower(): #lowercase it to minimize error
    if ch in alphabet: #this looks for elements in the txt file that are in the alphabet 
        freq_dict[ch] = freq_dict.get(ch, 0) + 1 #if it finds an element in the alaphebet, it'll add 1 to the total

lst = [] #creates list 
for key, value in freq_dict.items(): 
    lst.append((value,key)) 

lst.sort(reverse=True)
for freq, letter in lst: #finds out how many times the letter of the alphabet appears 
    print(letter, freq) #prints the letter of the alphabet and how many times it appears