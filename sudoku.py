def input_matrix(n = 9):
    mat = []
    for _ in range(n):
        mat.append([int(elem) if elem != "." else elem for elem in input().split()])
    return mat
print("Input 9*9 matrix,put '.' in the empty space:  ")
def output_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end = " ")
        print()


def find_empty(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == ".":
                return i,j

def is_valid(mat,num,pos_x,pos_y):
    #check row - syun
    for j in range(len(mat[0])):
        if mat[pos_x][j] == num:
            return False
    #chech col - tox
    for i in range(len(mat)):
        if mat[i][pos_y] == num:
            return False
    #check cube - 3*3 matrix

    box_x, box_y = pos_x //3 * 3, pos_y //3 * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if mat[i][j] == num:
                return False
    return True

def solve(mat):
    pos = find_empty(mat)
    if not pos:
        return True
    i , j = pos
    for num in range(1,10):
        if is_valid(mat,num,i,j):
            mat[i][j] = num
            if solve(mat):
                return True
            mat[i][j] = "."
    return False

matrix = input_matrix(9)
solve(matrix)
output_matrix(matrix)