#CLI instruktioner för spelarna
print("\nVälkommen till spelet ChokladAsken.\n")
print("Målet med spelet är att inte äta chokladrutan med värdet P. Poison chokladbiten.")
print("När det är din tur väljer du en ruta genom att skriva in värdet på rutan i terminalen.")
print("Alla rutor till höger och under om denna ruta kommer då att ätas.")
print("Därefter är det Spelare 2 tur att välja en ruta och äta.")
print("Detta fortsätter till en av spelarna tvingas äta Poison chokladbiten och förlorar.\n")
print("Lycka till!\n")
input("Tryck mellanslag för att börja.\n")

#Sätt upp hur många rader och kolumner.
matrix_input_valid = False

#Vi sätter upp en lista av de giltiga inmatnings integerna i strängform
valid_numbers = ["0","1","2","3","4","5","6","7","8","9"]

def validate_matrix_input(input):
    if input not in valid_numbers:
        return False
    return True

matrix_width = ""
matrix_height = ""

while not matrix_input_valid:
    matrix_width = input("Hur många rader ska chokladbaren bestå av: ")
    matrix_height = input("Hur många kolumer ska chokladbaren bestå av: ")
    if validate_matrix_input(matrix_width) and validate_matrix_input(matrix_height):
        matrix_input_valid = True
        matrix_width = int(matrix_width)
        matrix_height = int(matrix_height)
    else:
        print("Inmata ett giltigt nummer. Testa igen.")



#Här skapar vi matrisen och sätter alla dess värden till 0.
matrix = [[0 for x in range(matrix_width)] for y in range(matrix_height)]

#Här fyller vi matrisen med tiotals värden så att CLI matrisen får (ganska) jämnt utseende.
fill_integers = 10
for i in range(0,matrix_width):
    for j in range(0,matrix_height):
        matrix[i][j] = fill_integers
        fill_integers+=1

#Vi sätter värdet längst upp till vänster till poison värdet (P).
matrix[0][0] = "P"


#Funktion för att testa om inmatningen är giltig
#Returnar den 'False' är det något fel på användarens inmatningsvärde
def validate_input(input):
    #Den får inte vara tom
    if input=="":
        print("You entered nothing. Try again.")
        return False
    #Den får inte vara P
    if input=="P":
        print("Self-destruction not allowed. Try again.")
        return False
    #Testa om alla symboler ingår i listan, det vill säga är integers
    for char in input:
        if char not in valid_numbers:
            print("Only integers are accepted. Try again.")
            return False
    #Om allt innan har passerat så testar vi om inmatningen finns i matrisen.
    #Om input är större än höjd gånger bredd + 10 - 1 så är den utanför inmatningsgränserna.
    is_in_matrix = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if int(input) == matrix[i][j]:
                is_in_matrix = True
    return is_in_matrix

def player_action(value):
    global matrix
    #Hämta index
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] == value:
                row_index = i
                col_index = j
    #Ta bort alla under och till höger
    for k in range(row_index,len(matrix)):
        matrix[k] = matrix[k][:col_index] 
    
    #Om en rad är helt tom så tas den bort från arrayn
    matrix = [row for row in matrix if row]  



#Gameloop
play_again_bool = False
def game():
    global play_again_bool
    play_again_bool = False
    
    #Loop
    while True:
        #Om tidigare drag resulterade i att spelare 1 förlorade, vann spelare 2
        if len(matrix) == 1 and len(matrix[0]) == 1:
            print("Spelare 2 vann")
            break
        input_is_valid = False
        while not input_is_valid:
            print("")
            for row in range(0,len(matrix)):
                print(matrix[row])
            print("\nSpelare 1 tur")
            choice = input("Välj en ruta: \n")
            if validate_input(choice):
                input_is_valid = True
                player_action(int(choice))

        if len(matrix) == 1 and len(matrix[0]) == 1:
            print("Spelare 1 vann")
            break
        input_is_valid = False
        while not input_is_valid:
            print("")
            for row in range(0,len(matrix)):
                print(matrix[row])
            print("\nSpelare 2 tur")
            choice = input("Välj en ruta: \n")
            if validate_input(choice):
                input_is_valid = True
                player_action(int(choice))  

    restart = input("För att spela igen inmata 1. För att stänga programmet tryck ENTER.")    
    if restart == "1":
        play_again_bool = True  
game() 

#Återställ matrisen till sitt ursprunliga tillstånd
while play_again_bool:

    matrix = None
    matrix = [[0 for x in range(matrix_width)] for y in range(matrix_height)]

    fill_integers = 10
    for i in range(0,matrix_width):
        for j in range(0,matrix_height):
            matrix[i][j] = fill_integers
            fill_integers+=1

    matrix[0][0] = "P"  
    #starta gameloopen igen
    game()

