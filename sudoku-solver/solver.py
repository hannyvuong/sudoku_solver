



# board = [[8,0,6,0,9,0,0,0,0],
#          [0,0,0,2,0,0,8,0,0],
#          [5,9,0,0,0,0,0,6,1],
#          [0,0,0,7,1,0,6,0,4],
#          [0,5,0,0,6,0,0,0,0],
#          [0,0,7,9,0,0,0,8,2],
#          [7,2,5,0,3,8,9,0,6],
#          [6,0,4,0,7,9,1,2,3],
#          [0,1,0,0,2,4,0,0,0]]

def solve(board):
    
    #If no more empty spots, board filled therefore solution
    find = empty_spot(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid_number(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0

    return False
    


def valid_number(board, guess, position):

    #Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == guess and position[1] != i:
            return False
        
    #Check column
    for i in range(len(board)):
        if board[i][position[1]] == guess and position[0] != i:
            return False
    
    #Check box
    x = position[1] // 3
    y = position[0] // 3

    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if board[i][j] == guess and (i,j) != position:
                return False
    
    return True

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def empty_spot(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
            