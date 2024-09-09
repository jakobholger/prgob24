import random
 
#Hämta data från användaren gällande antal tärning och kast
dices = int(input("Hur många tärningar behövs i spelet? "))
throws = int(input("Hur många kast får en spelare? "))

def print_list(input_list):
    string_list = ""
    for i in range(0,len(input_list)-1): #För varje index till den näst sista
        string_list += str(input_list[i]) + ", "
    string_list += str(input_list[-1]) #Lägg till sista utan extra kommatecken
    return string_list

is_running = True #while loop boolean för att kunna stoppa loopen
while is_running:
    throws_list = []   
    print("\nGenom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A: ",end="")  
    for i in range(1,dices+1): #En loop som går från ett till det användaren matade in
        throw = input() #Kast
        if throw == "": #Kolla om det endast är ett mellanslag användaren matade in, isåfall generera tal
            generated_throw = random.randint(1,6)
            print("Tärning", i, ":", generated_throw, end="")
            throws_list.append(generated_throw)
        elif throw == "A": #Om det var ett A som inmatning, sätt is_running till falsk vilket gör att loopen stannar och breaka ur for loopen.
            print("Tack och hej!")
            is_running = False
            break

    if not is_running: #Lämna loopen om det som hände innan gjorde att is_running nu är falskt, detta gör att programmet tar slut
        break
    
    #Om vi inte lämnade loopen så ska vi printa ut kasten som vi fick som ligger lagrade i listan
    throws_string = print_list(throws_list)
    print("\nDu fick", throws_string)

    throw_again = throws-1 #Vi har redan gjort ett kast, därför throws-1
    while throw_again>0: #Medans throw_again är större än noll så har vi möjlighet att kasta igen
        print("\nÄr du inte nöjd kan du kasta igen, vill du kasta igen?(j/n) ",end="")  
        choice = input()
        if choice == "j": #Om användaren matade in j, alltså att de vill kasta igen så träffar denna if sats.
            print("Kasta")
            throws_list = []
            #Allt här samma som innan
            for i in range(1,dices+1): #
                throw = input()
                if throw == "":
                    generated_throw = random.randint(1,6)
                    print("Tärning", i, ":", generated_throw, end="")
                    throws_list.append(generated_throw)

            throws_string = print_list(throws_list)
            print("\nDu fick", throws_string)
        #Om de inte vill kasta igen så bryter vi throw_again while loopen.
        elif choice=="n":
            break
        throw_again-=1