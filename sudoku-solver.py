'''
Sudoku solver using backtracking algorithm
'''

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == 0:
                return (i, j) #row, column
    return None

def is_valid(b, num , pos): #board, number we insert, position

    #Check row - loop through every single col in row and check if the number we inserted is valid
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i: # 2nd condition is to skip the number we have just inserted
            return False #returning false if it is not valid

    #Check column - loop through every row, the same as above
    for j in range(len(b)):
        if b[j][pos[1]] == num and pos[0] != j:
            return False

    #Check the 3x3 box
        #checking in which box are we
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #loop through this box and check if the elements are not duplicated
    for i in range(box_y*3, box_x*3 + 3):
        for j in range(box_x * 3, box_y * 3 + 3):
            if b[i][j] == num and i != pos[0] and j != pos[1]: #or (i, j) != pos
                return False

    return True #like else - if everyting is fine



def solve(b): #solving the board using recursion
    find = find_empty(b) #if the function finds a empty place, it returns something, thus the value of find is True
    if not find:
        return True #the solution is found
    else:
        row, col = find

    for i in range(1,10): #check if by adding this nums to the board, the solution is valid
        if is_valid(b, i, (row, col)): #if it's valid:
            b[row][col] = i #add the num to the solution

            if solve(b): #try to solve it now with the new value
                return True #and if it solved return True

            b[row][col] = 0

    return False


def pprint_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')
        for j in range(len(b[i])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            if j == 8:
                print(b[i][j])
            else:
                print(b[i][j], end=' ')


print('Board before')
pprint_board(board)
solve(board)
print('\nBoard after')
pprint_board(board)

