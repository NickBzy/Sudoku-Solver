""" sudokuSolver.py solves sudoku boards using a backtracking algorithm """
_author_ = "Nicolas Buu"

#initiating sudoku board
board = [
    [0,1,0,8,0,0,0,0,2],
    [0,5,0,0,0,3,9,0,0],
    [4,0,8,5,0,0,0,0,0],
    [5,4,0,0,0,0,0,0,6],
    [0,6,1,0,0,0,4,9,0],
    [9,0,0,0,0,0,0,2,3],
    [0,0,0,0,0,9,2,0,8],
    [0,0,9,2,0,0,0,4,0],
    [1,0,0,0,0,8,0,5,0]
]
board2 = [
    [0,0,0,2,0,0,0,0,7],
    [0,0,0,5,0,0,0,0,6],
    [8,0,9,0,0,0,1,0,0],
    [1,6,0,8,0,2,3,0,9],
    [0,0,8,0,0,0,6,0,0],
    [2,0,3,6,0,5,0,4,1],
    [0,0,1,0,0,0,4,0,2],
    [4,0,0,0,0,8,0,0,0],
    [9,0,0,0,0,1,0,0,0]
]
#functions that prints board with horizontal and vertical borders
def print_board(board):
    """
    Function prints board with horizontal and vertical lines

    :board (parameter): 2d array representing sudoku board to solve
    """
    #iterates through number of rows
    for i in range(len(board)):
        #Prints a horizontal line every 3 rows
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - ")

        #iterates through number of columns
        for j in range(len(board[0])):
            #Prints a vertical line every 3 column
            if j%3 == 0 and j!=0:
                print(" | ", end="")

            #If loop is at last column, print element and go to next line
            if j==8:
                 print(board[i][j])
            #Otherwise, print element without skipping line
            else:
                 print(str(board[i][j]) + " ", end="")
                    

def find_empty(board):
    """
    Function goes through board and checks for empty cells

    :board (parameter): 2d array representing sudoku board to solve
    :return: coordinate of cell that is empty(0) in board
    """
    #Goes through board and checks which cell is equal to zero, if no empty cells, return none
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]==0):
                return (i,j)
    
    return None

def valid(board, num_inserted, pos):
    """
    Function that checks that number inserted is valid, meaning:
    - no same number on same horizontal line AND
    - no same number on same vertical line AND
    - no same number in same 3x3 sub-box of board

    :board(parameter): 2d array representing sudoku board to solve
    :num_inserted(parameter): integer inserted to try to solve board
    :pos(parameter): tuple with x and y coordinates of cell
    :return: returns false if not valid, returns true if valid
    """
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] ==num_inserted and pos[1] != i:
            return False
    #check column
    for i in range(len(board)):
        if board[i][pos[1]]== num_inserted and pos[0] != i:
            return False
    #Check which sub-box cell belongs to
    sub_box_x= pos[1]//3
    sub_box_y= pos[0]//3
    #Check sub-box
    for i in range(sub_box_y*3, sub_box_y*3 +3):
        for j in range(sub_box_x*3, sub_box_x*3 + 3):
            if(board[i][j]==num_inserted and (i,j) != pos):
                return False
    #True if it goes through all the checks 
    return True

def solve(board):
    """
    Function that solves the sudoku board recursively using backtracking

    :board(parameter): 2d array representing sudoku board to solve
    :return: returns true if all cells are filled in, retuns false if solution does not exist

    """
    #Checks if board has any empty cells
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    #tries number 1 through 9 for each empty cells
    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col]= i
            #recursive call to itself
            if solve(board):
                return True

            board[row][col]=0

    return False

    
    
print("")
print("Welcome to the Sudoku Solver")
print("Boards before solving:")
print("1)")
print_board(board)
print("")
print("2)")
print_board(board2)
print(" ")
while True:
    try:
        board_chosen= int(input("Which board would you like to solve: "))
    except ValueError:
        print("Invalid input, please try again!")
        continue
    if board_chosen<1 or board_chosen>2:
        print("Invalid choice, please select a number between 1 and 2!")
        continue
    else:
        break
if board_chosen==1:
    solve(board)
    print("Solved board:")
    print_board(board)
elif board_chosen==2:
    solve(board2)
    print("solved board:")
    print_board(board2)

print("Thank you for using the sudoku solver!")