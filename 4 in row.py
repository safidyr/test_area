board = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]

def show ():
    print (board[0],'','|',board[1],'','|',board[2],'','|',board[3],'','|',board[4],'','|',board[5],'','|',board[6],'','|')
    print ('__________________________________')
    print (board[7],'','|',board[8],'','|',board[9],'','|',board[10],'|',board[11],'|',board[12],'|',board[13],'|')
    print ('__________________________________')
    print (board[14],'|',board[15],'|',board[16],'|',board[17],'|',board[18],'|',board[19],'|',board[20],'|')
    print ('__________________________________')
    print (board[21],'|',board[22],'|',board[23],'|',board[24],'|',board[25],'|',board[26],'|',board[27],'|')
    print ('__________________________________')
    print (board[28],'|',board[29],'|',board[30],'|',board[31],'|',board[32],'|',board[33],'|',board[34],'|')
    print ('__________________________________')
    print (board[35],'|',board[36],'|',board[37],'|',board[38],'|',board[39],'|',board[40],'|',board[41],'|')

def drop_piece ():
    pass

def is_valid_location (board, col):
    pass

def get_next_open_row ():
    pass
    
    


game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = input('player one make your selection(0-6):')
        col = int(selection)
        
        print(selection)

    else:
        col = input('player two make a selection (0-6):')
        col = int(selection)

    turn += 1
    turn = turn % 2

show()
