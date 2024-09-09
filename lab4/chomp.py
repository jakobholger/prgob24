#Funktioner
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
            matrix[i][j] = str(10*row_integer+col_integer) #Strängar av 10*raden + kolumheltalet
            col_integer+=1
        row_integer+=1
    matrix[0][0] = "P"
    return matrix

def print_chocolate_bar(matrix):
    for row in matrix:
        for col in row:
            print(f"{col:>3}",end="") #Se till att outputen är formatterad med strängar som är 3 karaktärer långa
        print()
    return None

def chomp(matrix, row_index, col_index):
    if row_index<0 or col_index<0:
        return None

    #Ta bort alla under och till höger
    for k in range(row_index,len(matrix)):
        matrix[k] = matrix[k][:col_index] 
    
    #Om en rad är helt tom så tas den bort från arrayn
    matrix = [row for row in matrix if row]

    if not matrix: #Om den är tom retunera en tom lista
        return []
    return matrix

def check_winner(matrix):
    if len(matrix) == 1 and len(matrix[0])==1: #Om antalet antalet rader och kolumer är 1 så har någon vunnit.
        return True
    return False

def ask_cell_number(matrix):
    while True:
        try:
            # Be användaren mata in ett nummer
            user_input = input("Ange ett nummer som finns i matrisen: ")
            if user_input=="P":
                # Om indatan är P så är valueerrorn att man inte får förstöra för sig själv
                raise ValueError("Självförstörelse ej tillåtet, försök igen!")
            
            # Hitta rad och kolumn där numret finns
            for row in range(0,len(matrix)):
                for col in range(0,len(matrix[row])):
                    if user_input in matrix[row][col]:
                        return (row,col)

            # Om numret inte hittas i matrisen, kasta ett undantag
            raise ValueError("Fel val, ruta " + user_input + " finns inte i spelplanen, försök igen!")
        
        except ValueError as e:
            print(e)  # Skriv ut felmeddelandet och fråga igen

#Funktion som frågar efter antalet rader och kolumer och returnerar de i int form om dem är giltiga
def prompt_matrix_size():
    #Vi sätter upp en lista av de giltiga inmatnings integerna i strängform för matrisen
    valid_numbers = ["2","3","4","5","6","7","8","9"]

    matrix_width = ""
    matrix_height = ""

    matrix_input_valid = False

    while not matrix_input_valid:
        matrix_width = input("Hur många rader ska chokladbaren bestå av (2-9): ")
        matrix_height = input("Hur många kolumer ska chokladbaren bestå av (2-9): ")
        if matrix_width in valid_numbers and matrix_height in valid_numbers:
            matrix_input_valid = True
            return int(matrix_width),int(matrix_height)
        else:
            print("Inmata ett giltigt nummer. Testa igen.")
