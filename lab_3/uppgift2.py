#En lista av alla nummer i strängform.
valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#Denna funktion tar ett input och kollar om det endast innehåller integers genom att jämföra med strängversionerna av den.
def validate_input(input):
    if input not in valid_numbers:
        return False
    return True

input_is_valid = False
    
# Kontrollera att värdena är inom det angivna intervallet
# Fråga efter antalet rader och kolumner
while not input_is_valid:
    
    rows = input("Ange antal rader: ")
    cols = input("Ange antal kolumner: ")

    if validate_input(rows) and validate_input(cols): #Om båda rows and cols var korrekta inputs, fortsätt.

        #Sätt input_is_valid = True för att stoppa while loopen
        input_is_valid = True

        # Gör om inputsen till integers.
        rows = int(rows)
        cols = int(cols)

        # Rubrikraden
        print("  ", end="")
        col_counter = 1
        while col_counter <= cols:
            print(f"{col_counter:>3}", end="") #Lägg till 'padding' så att stränglängden blir 3 om den innan var kortare än 3
            col_counter += 1
        print()
        
        # Raderna med multiplikationstabellen
        row_counter = 1
        while row_counter <= rows:
            print(f"{row_counter:<2}", end="")  # Skriv ut radnumret
            col_counter = 1
            while col_counter <= cols:
                print(f"{row_counter * col_counter:>3}", end="")
                col_counter += 1
            print()  # Gå till nästa rad
            row_counter += 1
    else:
        print("Felaktig inmatning. Värdena måste vara mellan 1 och 9.")
