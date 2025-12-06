from motor_enigma import carregar_fitxer, desxifrar_missatge
import utils as ut
#LLIBRERIA DE CONSTANTS
import constants as c
def main():
    opcio = '0'
    while opcio != '4':
        rotor1 = carregar_fitxer(c.RUTA_ROTOR1) #afegim com a variable cada rotor per si l'usuari escogeix l'opcio de editar rotors
        rotor2 = carregar_fitxer(c.RUTA_ROTOR2) #aixi un coop torni a sortir el menu tindra les dades actulitzades
        rotor3 = carregar_fitxer(c.RUTA_ROTOR3)

        ut.netejar_pantalla()
        print("\nENIGMA")
        print("--------------")
        print("1. Xifrar missatge")
        print("2. Desxifrar missatge")
        print("3. Editar rotors")
        print("4. Sortir")
        opcio = input("Selecciona una opcio: ")

        if opcio == '1':
            ut.netejar_pantalla()
            print("XIFRAR MISSATGE")
            configuracio = input("Introdueix la configuracio inicial: ") #per la configuracio de l'usuari que haura de posar 3 lletres
            missatge = input("Introdueix el missatge que vulguis xifrar:")
            missatge = missatge.upper() #per posar-ho tota majuscules el missatge

            lletres_valides = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            missatge_buit = "" #es la variable per guardar nomes les lletres i no numeros o caracters especials
            for lletra in missatge:
                if lletra in lletres_valides:
                    missatge_buit += lletra
            
            missatge = missatge_buit
            missatge_xifrat = xifrar_missatge(missatge,rotor1,rotor2,rotor3,configuracio)
            print(f"resultat: {missatge_xifrat}")
            with open ('missatge.txt', 'w') as f:
                f.write(missatge_xifrat)
        elif opcio == '2':
            ut.netejar_pantalla()
            print("DESXIFRAR MISSATGE")
            configuracio = input("Introdueix la configuracio inicial: ")

            with open("data/Missatge.txt", 'r') as f:
                missatge = f.read().strip()

            print(f"Missatge xifrat llegit des del fitxer: {missatge}")
            missatge_desxifrat = desxifrar_missatge(missatge, rotor1, rotor2, rotor3, configuracio)
            print(missatge_desxifrat)
            input("\nPremeu qualsevol tecla per a continuar. . .")

        elif opcio == '3':
            print("EDITAR ROTORS")

        elif opcio == '4':
            print("Has sortit")

main()