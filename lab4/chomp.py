def create_chocolate_bar(row, col):
    if row<=0 or col<=0:
        return None
    #Här skapar vi matrisen och sätter alla dess värden till 0.
    matrix = [[0 for x in range(col)] for y in range(row)]

    #Här fyller vi matrisen med tiotals värden så att CLI matrisen får (ganska) jämnt utseende.
    row_integer=1
    for i in range(0,row):
        col_integer=1
        for j in range(0,col):
            matrix[i][j] = 10*row_integer+col_integer
            col_integer+=1
        row_integer+=1
    return matrix

def print_chocolate_bar(matrix):
    for row in matrix:
        for col in row:
            print(f"{col:>3}",end="")
        print()
    return None

def chomp(matrix, row_index, col_index):
    row_index = int(row_index)
    col_index = int(col_index)
    if row_index<0 or col_index<0:
        return None


    #Ta bort alla under och till höger
    for k in range(row_index,len(matrix)):
        matrix[k] = matrix[k][:col_index] 
    
    #Om en rad är helt tom så tas den bort från arrayn
    matrix = [row for row in matrix if row]

    if not matrix:
        return []
    return matrix
