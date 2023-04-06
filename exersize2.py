
fhand = open("exersize.txt", 'r') #open the file 
hours_of_day = {} #creates dictionary 
#hours_of_day.get()
for line in fhand: 
    if line.startswith("From "):
        time = line.split()[5] #gets the time hh:mm:ss  
        hour = time.split(":")[0]#getting the zeroth element which is the hour. 
        hours_of_day[hour] = hours_of_day.get(hour, 0) + 1 #looks for the hour, but if it cant find it, then it puts in a 1.
        print("time: "+ time)
        print("hour:" +hour) 
        print("line: " +line)
        print("debug:" + str(hours_of_day.get(hour, 0)))

lst = list(hours_of_day.items())
lst.sort()
for t in lst:
    print(t[0], t[1])
   
