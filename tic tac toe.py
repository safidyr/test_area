import random

board = [0,1,2,3,4,5,6,7,8]

def show ():
    print (board[0],'|',board[1],'|',board[2],'|')
    print ('___________')
    print (board[3],'|',board[4],'|',board[5],'|')
    print ('___________')
    print (board[6],'|',board[7],'|',board[8],'|')

def checkLine(char,spot1,spot2,spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True
    
def checkAll(char):
    if checkLine(char,0,1,2):
        True 
    if checkLine(char,1,4,7):
        True  
    if checkLine(char,2,5,8):
        True
    if checkLine(char,6,7,8):
        True 
    if checkLine(char,3,4,5):
        True  
    if checkLine(char,2,4,6):
        True  
    if checkLine(char,0,4,8):
        True

while True:
    
    inp = input('Select a spot:')
    inp = int(inp)
    
    if board[inp] != 'x' and board[inp] != 'o':
        board[inp] = 'x'

        if checkAll('x') == True:
            print('X wins!')
            break
           
           
        while True:
            random.seed
            opponent = random.randint(0,8)

            if board[opponent] != 'o' and board[opponent] != 'x':
                board[opponent] = 'o'
                
                if checkAll('o') == True:
                    print('O wins!')
                    break
            
                
               
    else:
        print('This spot is taken')

    show()

