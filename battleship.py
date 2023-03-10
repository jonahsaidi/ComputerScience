'''
Created on Nov 30, 2022

@author: jsaidi24
    algorithm:
    print 2 boards for human 
    print 2 boards for computer 
    input position of ships for human board 
    input position of ships for computer player(randomize) 
    take shot on your opponent
    (update board, check for hit or miss)
    computer shoots back 
    (update board, check for hit or miss)
    check winner
    after win, game over.    
    
'''

from random import randint
import random

def computer_check(user_choice,computer_board,player_hits,player_shots):# passing through multiple variables 
    
    

    if user_choice == 'A1':                    #setting the condition if the choice is A1
        if computer_board[0][0]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[0][0]= 'X' #co-ordinates of A1
        else:
            print("miss!")

    elif user_choice == 'A2':           #setting the condition if the choice is A2
        if computer_board[0][1]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[0][1]= 'X'#co-ordinates of A2
        else:
            print("miss!")
            
    elif user_choice == 'A3':           #setting the condition if the choice is A3
        if computer_board[0][2]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[0][2]= 'X'#co-ordinates of A3
        else:
            print("miss!")
            
            
    elif user_choice == 'A4':           #setting the condition if the choice is A4
        if computer_board[0][3]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[0][3]= 'X'#co-ordinates of A4
        else:
            print("miss!")
            
    elif user_choice == 'A5':                       #setting the condition if the choice is A5
        if computer_board[0][4]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[0][4]= 'X'#co-ordinates of A5
        else:
            print("miss!")        
            
            
    elif user_choice == 'B1':                       #setting the condition if the choice is B1
        if computer_board[1][0]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[1][0]= 'X'#co-ordinates of B1
        else:
            print("miss!")        
            
    elif user_choice == 'B2':                   #setting the condition if the choice is B2
        if computer_board[1][1]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[1][1]= 'X'#co-ordinates of B2
        else:
            print("miss!")        
            
            
    elif user_choice == 'B3':               #setting the condition if the choice is B3
        if computer_board[1][2]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[1][2]= 'X'#co-ordinates of B3
        else:
            print("miss!")        
            
            
            
    elif user_choice == 'B4':               #setting the condition if the choice is B4
        if computer_board[1][3]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[1][3]= 'X'#co-ordinates of B4
        else:
            print("miss!")        
            
    elif user_choice == 'B5':               #setting the condition if the choice is B5
        if computer_board[1][4]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[1][4]= 'X'#co-ordinates of B5
        else:
            print("miss!")        
            
    elif user_choice == 'C1':           #setting the condition if the choice is C1
        if computer_board[2][0]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[2][0]= 'X'#co-ordinates of C1
        else:
            print("miss!")        
            
    elif user_choice == 'C2':           #setting the condition if the choice is C2
        if computer_board[2][1]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[2][1]= 'X'#co-ordinates of C2
        else:
            print("miss!")        
                   
           
    elif user_choice == 'C3':           #setting the condition if the choice is C3
        if computer_board[2][2]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[2][2]= 'X'#co-ordinates of C3
        else:
            print("miss!")       
           
    elif user_choice == 'C4':           #setting the condition if the choice is C4
        if computer_board[2][3]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[2][3]= 'X'#co-ordinates of C4
        else:
            print("miss!")       
                  
           
    elif user_choice == 'C5':           #setting the condition if the choice is C5
        if computer_board[2][4]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[2][4]= 'X'#co-ordinates of C5
        else:
            print("miss!")       
           
           
    elif user_choice == 'D1':           #setting the condition if the choice is D1
        if computer_board[3][0]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[3][0]= 'X'#co-ordinates of D1
        else:
            print("miss!") 
    
    
    elif user_choice == 'D2':           #setting the condition if the choice is D2
        if computer_board[3][1]== "S":
            print("Hit!")
            player_hits += 1        #adds to the total hit count
            player_shots[3][1]= 'X'#co-ordinates of D2
        else:
            print("miss!")      
           
           
    elif user_choice == 'D3':           #setting the condition if the choice is D3
        if computer_board[3][2]== "S":
            print("Hit!")
            player_hits += 1    #adds to the total hit count
            player_shots[3][2]= 'X'#co-ordinates of D3
        else:
            print("miss!")       
           
           
    elif user_choice == 'D4':           #setting the condition if the choice is D4
        if computer_board[3][3]== "S":
            print("Hit!")
            player_hits += 1    #adds to the total hit count
            player_shots[3][3]= 'X'#co-ordinates of D4
        else:
            print("miss!")       
                   
           
    elif user_choice == 'D5':               #setting the condition if the choice is D5
        if computer_board[3][4]== "S":
            print("Hit!")
            player_hits += 1    #adds to the total hit count
            player_shots[3][4]= 'X'#co-ordinates of D5
        else:
            print("miss!")       
           
    elif user_choice == 'E1':           #setting the condition if the choice is E1
        if computer_board[4][0]== "S":
            print("Hit!")
            player_hits += 1    #adds to the total hit count
            player_shots[4][0]= 'X'#co-ordinates of E1
        else:
            print("miss!")       
           
    elif user_choice == 'E2':           #setting the condition if the choice is E2
        if computer_board[4][1]== "S":
            print("Hit!")
            player_hits += 1    #adds to the total hit count
            player_shots[4][1]= 'X'#co-ordinates of E2
        else:
            print("miss!")       
           
           
    elif user_choice == 'E3':           #setting the condition if the choice is E3
        if computer_board[4][2]== "S":
            print("Hit!")
            player_hits += 1    #adds to the total hit count
            player_shots[4][2]= 'X'#co-ordinates of E3
        else:
            print("miss!")       
           
    elif user_choice == 'E4':           #setting the condition if the choice is E4
        if computer_board[4][3]== "S":
            print("Hit!")
            player_hits += 1    #adds to the total hit count
            player_shots[4][3]= 'X'#co-ordinates of E4
        else:
            print("miss!")       
           
    elif user_choice == 'E5':           #setting the condition if the choice is E5
        if computer_board[4][4]== "S":
            print("Hit!")
            player_hits += 1                #adds to the total hit count
            player_shots[4][4]= 'X'#co-ordinates of E5
        else:
            print("miss!")
           
    return player_hits
def player_check(battleboard,player_shots ):
    
    row= random.randint(0,4)        #the computer will choose random coordinates for the row 
    column = random.randint(0,4)    #the computer will choose random coordinates for the column 
    
    
    if battleboard[row][column] == 'S':  #this is the condition in which your ship is sunk 
        print("sunk your ship ")         #Message so the player knows that their battleship is sunk 
        
 
def randplace(battleboard):
    
    counter = 0     #set counter to 0
    
    while counter < 4:              
        
        row = randint(0, 4)     #the computer will choose random coordinates for the row
        col = randint(0, 4)     #the computer will choose random coordinates for the column
        
        battleboard[row][col] = "S " #if the row and column equal an 'S', then the counter will go up 1
        counter +=1
        
    print("\n\n\n")         #better spacing for UI
    

def PrintBoard(battleboard):      
    r=0         #setting to 0 
    c=0         #setting to 0
    while r < 5:            #conditional and a while 
        c=0             
        while c < 5:
            print(battleboard[r][c], end = " ")       
            c = c + 1
        r = r + 1
        print("\n")         #better spacing for UI
  
    
def main():
    
    winner_counter=0            #set all to 0
    player_hits=0
    miss_counter =0 
    
    print('welcome to battle ship')#nice friendly message to user
    battleboard =[["A1", "A2", "A3", "A4", "A5"],                     #for the human player
                  ["B1", "B2", "B3", "B4", "B5"],
                  ["C1", "C2", "C3", "C4", "C5"],
                  ["D1", "D2", "D3", "D4", "D5"], 
                  ["E1", "E2", "E3", "E4", "E5"]]
    
    computer_board =[["A1", "A2", "A3", "A4", "A5"],                     #for the human player
                  ["B1", "B2", "B3", "B4", "B5"],
                  ["C1", "C2", "C3", "C4", "C5"],
                  ["D1", "D2", "D3", "D4", "D5"], 
                  ["E1", "E2", "E3", "E4", "E5"]]
    
    computer_shots =[["A1", "A2", "A3", "A4", "A5"],                     #for the human player
                  ["B1", "B2", "B3", "B4", "B5"],
                  ["C1", "C2", "C3", "C4", "C5"],
                  ["D1", "D2", "D3", "D4", "D5"], 
                  ["E1", "E2", "E3", "E4", "E5"]]
    
    player_shots =[["A1", "A2", "A3", "A4", "A5"],                     #for the human player
                  ["B1", "B2", "B3", "B4", "B5"],
                  ["C1", "C2", "C3", "C4", "C5"],
                  ["D1", "D2", "D3", "D4", "D5"], 
                  ["E1", "E2", "E3", "E4", "E5"]]
    PrintBoard(battleboard)
    print("\n\n\n")  #spaces in between in order to create breathing room for the UI
    PrintBoard(computer_board)
    print("\n\n\n")#spaces in between in order to create breathing room for the UI
    PrintBoard(computer_shots)
    print("\n\n\n")#spaces in between in order to create breathing room for the UI
    PrintBoard(player_shots)
    print("\n\n\n")#spaces in between in order to create breathing room for the UI
    
    randplace(battleboard)
    randplace(computer_board)
    
    print("this is the battle board")
    PrintBoard(battleboard)
    
    print("this is the computer board")
    PrintBoard(computer_board)
    
    
    user_choice= input("which co-ordinate would you like to fire?").upper() #user choice, I made it .upper so it will automatically convert any letter into upper case, eliminated possible bugs.
    
    player_hits = computer_check(user_choice, computer_board, player_hits, player_shots)
    
if __name__ == '__main__':
    main()