from motor_enigma import carregar_fitxer

def main():
    opcio = '0'
    while opcio != '4':
        rotor1 = carregar_fitxer("Rotor1.txt") #afegim com a variable cada rotor per si l'usuari escogeix l'opcio de editar rotors
        rotor2 = carregar_fitxer("Rotor2.txt") #aixi un coop torni a sortir el menu tindra les dades actulitzades
        rotor3 = carregar_fitxer("Rotor3.txt")

        print("\nENIGMA")
        print("--------------")
        print("1. xifrar missatge")
        print("2.desxifrar missatge")
        print("3. editar rotors")
        print("4.sortir")
        opcio = input("selecciona una opcio: ")

        if opcio == '1':
            configuracio = input("introdueix la configuracio inicial")
            missatge = input("introdueix el missatge que vulguis xifrar")
            missatge = missatge.upper() #per posar-ho tota majuscules el missatge

            lletres_valides = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            missatge_buit = "" #es la variable per guardar nomes les lletres i no numeros o caracters especials
            for lletra in missatge:
                if lletra in lletres_valides:
                    missatge_buit += lletra
            
            missatge = missatge_buit

        if opcio == '4':
            print("has sortit")

main()