from chomp import *

#CLI instruktioner för spelarna
print("\nVälkommen till spelet Chomp.\n")
print("Målet med spelet är att inte äta chokladrutan med värdet P. Poison chokladbiten.")
print("När det är din tur väljer du en ruta genom att skriva in värdet på rutan i terminalen.")
print("Alla rutor till höger och under om denna ruta kommer då att ätas.")
print("Därefter är det Spelare 2 tur att välja en ruta och äta.")
print("Detta fortsätter till en av spelarna tvingas äta Poison chokladbiten och förlorar.\n")
print("Lycka till!\n")
input("Tryck ENTER för att börja.\n")

matrix_width, matrix_height = prompt_matrix_size()

matrix = create_chocolate_bar(matrix_width, matrix_height)

#Gameloop
def game(matrix): 
    #Loop
    while True:
        print()
        print_chocolate_bar(matrix)
        print("\nSpelare 1 tur")
        row,col = ask_cell_number(matrix)
        matrix = chomp(matrix,row,col)

        if check_winner(matrix):
            print("Spelare 1 vann")
            break
        print()
        print_chocolate_bar(matrix)
        print("\nSpelare 2 tur")
        row,col = ask_cell_number(matrix)
        matrix = chomp(matrix,row,col) 

        #Om tidigare drag resulterade i att spelare 1 förlorade, vann spelare 2
        if check_winner(matrix):
            print("Spelare 2 vann")
            break

game(matrix) #Inkalla funktionen

#Spela igen loop
while True:
    restart = input("För att spela igen inmata 1. För att stänga programmet tryck ENTER.")    
    if restart == "1":
        matrix_width,matrix_height = prompt_matrix_size()
        matrix = create_chocolate_bar(matrix_width,matrix_height)
        game(matrix)
    else:
        break
