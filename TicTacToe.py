'''
Created on Nov 15, 2022

@author: jsaidi24


check to see if has taken
check to see if spot 1-9

'''
from _operator import xor
from _ast import If
def print_board(board):     #function for the board 
    for i in board:             #this will print the board 
        print(i)
    
def main():
    
    print("Welcome to Tic Tac Toe")             #nice message to the user 
    board = [[1,2,3,],[4,5,6],[7,8,9]]          #this makes it easy for the user to pick a number 1-9, s its pretty straightforward 
    
    print("\n\n\n")     #adding some space so there is more clarity when printing and running the code 
    counter= 0              
    while counter < 5:              #the amount of times that that each turn can run before the board gets filled up
    #algo begins
        XO= "X"      #this is for the 'x' player
        
        while True:
            location = input("type in your choice for " + XO + ":")     #asking the user where they want to make their move
            ok = CheckPosition(board, location)
            
            print("44: " + str(ok))
           
            if ok == True:
                print("Position is already taken")
                continue
            else:
                UpdateBoard(board,location, "O")            #this makes sure that the board is up to date with the players moves
                break
                
        print_board(board)                      #simply printing the board 
        location = input("type in your choice for " + XO + ":")             #this is the input that the user will put in 
        
        UpdateBoard(board, location, "X")       #this will update the spaces in which the players have put their move
        winner = CheckWinner(board, XO)     #this is how the code will check who wins the game, and if someone has run. it will check every turn.
        print_board(board)      #printing the board 
        print("\n\n\n")         #extra spaces to see the game easier when running the code 
    
    ###################################################### this is to help show a visual break in the differences with the "x" code and the "o" code
    
        XO= "O"     #this is for the "o" player 
        
        
        while True:
            location = input("type in your choice for " + XO + ":")     #asking the user where they want to make their move
            ok = CheckPosition(board, location)
            
            print("44: " + str(ok))
           
            if ok == True:
                print("Position is already taken")
                continue
            else:
                UpdateBoard(board,location, "O")            #this makes sure that the board is up to date with the players moves
                break
                
        
        print_board(board)          #prints the board after it is updated. it is important that this step comes after. 
        
        print("\n\n\n")             #adds extra space on the board for the user to navigate clearly 
        
        winner = CheckWinner(board, XO)     #this calls the check winner function, so the code will check if someone has won the game every turn
        if winner == True:                  # this is the conditional if the "o" player wins 
            print(XO + "wins, good game!")      #message to the user that they won and that the game is over. 
            
def PrintBoard(board):      
    r=0         #setting to 0 
    c=0         #setting to 0
    while r < 3:            #conditional and a while 
        c=0             
        while c < 3:
            print(board[r][c], end = " ")       
            c = c + 1
        r = r + 1
    print(" ")
       
def UpdateBoard(board, location, XO):           #taking in variables 'board', 'location', and 'XO' 
    
    if location == "1":                         #setting the coordinates if the location is 1
        board[0][0] = XO
    elif location == "2":                       #setting the coordinates if the location is 2
        board [0][1] = XO
    elif location == "3":                       #setting the coordinates if the location is 3
        board [0][2] = XO
    elif location == "4":                       #setting the coordinates if the location is 4
        board [1][0] = XO                      
    elif location == "5":                       #setting the coordinates if the location is 5
        board [1][1] = XO
    elif location == "6":                       #setting the coordinates if the location is 6
        board [1][2] =XO
    elif location =="7":                        #setting the coordinates if the location is 7
        board [2][0] =XO
    elif location =="8":                        #setting the coordinates if the location is 8
        board [2][1] =XO
    elif location =="9":                        #setting the coordinates if the location is 9
        board [2][2] =XO

def CheckWinner(board, XO):
    
    winner = False
    
    if board[0][0]==XO and board[0][1]==XO and board[0][2] == XO:       #these are the three coordinates on the board in which a win will occur, this is 1 of 8 ways.
        winner = True
        print(XO + 'wins')
       
    elif board[1][0] ==XO and board [1][1] ==XO and board[1][2]== XO:   #these are the three coordinates on the board in which a win will occur, this is 1 of 8 ways.
        print(XO + 'wins')                              
    
    elif board[2][0] == XO and board[2][1]==XO and board[2][2]== XO:    #these are the three coordinates on the board in which a win will occur, this is 1 of 8 ways.
        print(XO + 'wins')
    
    elif board[0][0] == XO and board[1][0]== XO and board[2][0]== XO:   #these are the three coordinates on the board in which a win will occur, this is 1 of 8 ways.
        print(XO + 'wins')
    
    elif board[0][1] ==XO and board[1][1]== XO and board[2][1]==XO:     #these are the three coordinates on the board in which a win will occur, this is 1 of 8 ways.
        print(XO + 'wins')
    
    elif board[0][2]== XO and board[1][2] == XO and board[2][2]== XO:   #these are the three coordinates on the board in which a win will occur, this is 1 of 8 ways.
        print(XO + 'wins')
    
    elif board[0][0] == XO and board[1][1]== XO and board[2][2]== XO:   #these are the three coordinates on the board in which a win will occur, this is 1 of 8 ways.
        print(XO + 'wins')
    
    elif board[0][2] == XO and board[1][1] == XO and board[2][0] == XO: #these are the three coordinates on the board in which a win will occur, this is 1 of 8 ways.
        print(XO + 'wins')
        
    return winner           #need to return the winner

def CheckPosition(board, location):         #taking in the variables 'board' and 'location' 
    ok = False 
    
    if location == "1":
        if board[0][0] == 'X' or board[0][0] == 'O':            #making sure that this spot can only be taken once
            print("133")
            ok = True 
    
    elif location == "2":
        if board[0][1] == 'X' or board[0][1] == 'O':            #making sure that this spot can only be taken once
            ok = True        
            
    elif location == "3":
        if board[0][2] == 'X' or board[0][2] == 'O':            #making sure that this spot can only be taken once
            ok = True  
            
    elif location == "4":
        if board[1][0] == 'X' or board[1][0] == 'O':            #making sure that this spot can only be taken once
            ok = True    
            
    elif location == "5":
        if board[1][1] == 'X' or board[1][1] == 'O':            #making sure that this spot can only be taken once
            ok = True        
            
    elif location == "6":
        if board[1][2] == 'X' or board[1][2] == 'O':            #making sure that this spot can only be taken once
            ok = True  
            
    elif location == "7":
        if board[2][0] == 'X' or board[2][0] == 'O':            #making sure that this spot can only be taken once
            ok = True        
            
    elif location == "8":
        if board[2][1] == 'X' or board[2][1] == 'O':            #making sure that this spot can only be taken once
            ok = True        
            
    elif location == "9":
        if board[2][2] == 'X' or board[2][2] == 'O':            #making sure that this spot can only be taken once
            ok = True                        
           
    return ok

main()