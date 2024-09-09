#Importera TV från TV.py
from TV import TV

def read_file(file_name): #Funktion som läser från textfilen
    TV_list = []
    with open(file_name, "r") as file: #Öppnar filen för läsoperationer
        for row in file:
            item = row.strip().split(",") #Delar sträng
            TV_list.append(TV(item[0], int(item[1]), int(item[2]), int(item[3]), int(item[4])))
    return TV_list

def write_file(item_list, file_name): #Funktion som skriver till textfilen.
    with open(file_name, "w") as file:
        for item in item_list:
            file.write(item.str_for_file() + "\n")  # Se till att varje TV får en egen rad i textfilen.

# Läs data från allatv.txt filen med hjälp av denna funktion
tv_list = read_file("allatv.txt")


#Program logik körs här
print("***Välkommen till TV-simulatorn****")

def tv_prompt(choice):
    valid_operations = ["1","2","3","4"] 
    while True: #While true loop som kommer visa TV och dess attribut samt be användaren om indata
        
        print()
        print(tv_list[choice-1]) #Printa TV objektet som valts

        operation =  input("1. Byt kanal \n2. Sänk ljudnivå \n3. Höj ljudnivå\n4. Gå till huvudmenyn\nVälj: ")
        if operation in valid_operations: #Om strängen vid input finns i valid operations listan så fortsätt
            if operation == "1": #Om den är lika med 1 så ändra kanal
                channel = int(input("Inmata värde: "))
                if channel > tv_list[choice-1].max_channel or channel < 1: #Utanför rangen
                    input_channel = False
                    while not input_channel: #Fortsätt fråga användaren om indata tills indatan är giltig
                        channel = int(input("Kanal för den här TV:n ska vara mellan 1 till " + str(tv_list[choice].max_channel) + ", försök igen:"))
                        if tv_list[choice-1].change_channel(channel): #Om värdet var giltigt så stoppa while loopen med hjälp av att ändra booleanen.
                            input_channel = True
                else:
                    tv_list[choice-1].change_channel(channel)
            if operation == "2":
                tv_list[choice-1].decrease_volume()

            if operation == "3":
                tv_list[choice-1].increase_volume()
 
            if operation == "4": #Lämna whileloopen om användaren matade in 4 i som input.
                break

game_loop = True #Denna variabel används för att loopa default prompt som ger oss alternativen mellan varje TV och att avsluta programmet.

                
def default_prompt():

    global game_loop #Global för att vi ska du ha tillgång till variabeln.
    input_is_valid = False

    while not input_is_valid:
        i = 0
        valid_inputs = []

        print()

        while i<len(tv_list):
            valid_inputs.append(str(i+1))
            print(str(i+1) + ".", tv_list[i].tv_name) #Vi vill att listan i terminalen ska börja från 1 och måste därför offseta med ett värde av ett då ett list objekt börjar med index 0.
            i+=1
            
        valid_inputs.append(str(i+1)) #Det sista alternativet ska vara avsluta.
        print(str(i+1)+". Avsluta") #Adderar vi fler TV objekt kommer avsluta fortfarande vara sist. (Dynamiskt)
        choice = input("Välj: ")
        if choice in valid_inputs:
            input_is_valid = True
            choice = int(choice)
            if choice == i+1:
                game_loop = False
                break 
            tv_prompt(choice)
        else:
            print("\nEj giltig indata. Testa igen.\n")

while game_loop: #Avslutas genom att användaren inmatar värdet för att avsluta.
    default_prompt()


# Skriv in den modifierade listan i allatv.txt filen igen.
write_file(tv_list, "allatv.txt")
