#CLI instruktioner för spelarna
print("\nVälkommen till spelet Chomp.\n")
print("Målet med spelet är att inte äta chokladrutan med värdet P. Poison chokladbiten.")
print("När det är din tur väljer du en ruta genom att skriva in värdet på rutan i terminalen.")
print("Alla rutor till höger och under om denna ruta kommer då att ätas.")
print("Därefter är det Spelare 2 tur att välja en ruta och äta.")
print("Detta fortsätter till en av spelarna tvingas äta Poison chokladbiten och förlorar.\n")
print("Lycka till!\n")
input("Tryck ENTER för att börja.\n")

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
            matrix[i][j] = str(10*row_integer+col_integer)
            col_integer+=1
        row_integer+=1
    matrix[0][0] = "P"
    return matrix

def print_chocolate_bar(matrix):
    for row in matrix:
        for col in row:
            print(f"{col:>3}",end="")
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

    if not matrix:
        return []
    return matrix

def check_winner(matrix):
    if len(matrix) == 1 and len(matrix[0])==1:
        return True
    return False

def ask_cell_number(matrix):
    while True:
        try:
            # Be användaren mata in ett nummer
            user_input = input("Ange ett nummer som finns i matrisen: ")
            if user_input=="P":
                # Om numret inte hittas i matrisen, kasta ett undantag
                raise ValueError("Självförstörelse ej tillåtet, försök igen!")
            # Hitta rad och kolumn där numret finns
            for i, row in enumerate(matrix):
                if user_input in row:
                    # Returnera raden och kolumnen som tuple om numret hittas
                    return (i, row.index(user_input))
            
            # Om numret inte hittas i matrisen, kasta ett undantag
            raise ValueError("Fel val, ruta " + user_input + " finns inte i spelplanen, försök igen!")
        
        except ValueError as e:
            print(e)  # Skriv ut felmeddelandet och fråga igen


#Vi sätter upp en lista av de giltiga inmatnings integerna i strängform
valid_numbers = ["1","2","3","4","5","6","7","8","9"]

def validate_matrix_input(input):
    if input not in valid_numbers:
        return False
    return True

matrix_width = ""
matrix_height = ""

matrix_input_valid = False

while not matrix_input_valid:
    matrix_width = input("Hur många rader ska chokladbaren bestå av: ")
    matrix_height = input("Hur många kolumer ska chokladbaren bestå av: ")
    if validate_matrix_input(matrix_width) and validate_matrix_input(matrix_height):
        matrix_input_valid = True
        matrix_width = int(matrix_width)
        matrix_height = int(matrix_height)
    else:
        print("Inmata ett giltigt nummer. Testa igen.")

matrix = create_chocolate_bar(matrix_width, matrix_height)

#Gameloop
play_again_bool = False
def game(matrix):
    global play_again_bool
    play_again_bool = False
    
    #Loop
    while True:
        #Om tidigare drag resulterade i att spelare 1 förlorade, vann spelare 2
        if check_winner(matrix):
            print("Spelare 2 vann")
            break

        print("")
        print_chocolate_bar(matrix)
        print("\nSpelare 1 tur")
        row,col = ask_cell_number(matrix)
        matrix = chomp(matrix,row,col)

        if check_winner(matrix):
            print("Spelare 1 vann")
            break
        print("")
        print_chocolate_bar(matrix)
        print("\nSpelare 2 tur")
        row,col = ask_cell_number(matrix)
        matrix = chomp(matrix,row,col) 

    restart = input("För att spela igen inmata 1. För att stänga programmet tryck ENTER.")    
    if restart == "1":
        play_again_bool = True  
game(matrix) 

#Återställ matrisen till sitt ursprunliga tillstånd
while play_again_bool:
    matrix = create_chocolate_bar(matrix_width,matrix_height)
    game(matrix)

