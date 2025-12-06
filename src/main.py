from motor_enigma import carregar_fitxer, xifrar_missatge
import utils as ut

def main():
    rotor1 = carregar_fitxer("data/Rotor1.txt") #afegim com a variable cada rotor per si l'usuari escogeix l'opcio de editar rotors
    rotor2 = carregar_fitxer("data/Rotor2.txt") #aixi un coop torni a sortir el menu tindra les dades actulitzades
    rotor3 = carregar_fitxer("data/Rotor3.txt")

    opcio = '0'
    while opcio != '4':
        print("\nENIGMA") #el menu predeterminat de lamaquina
        print("--------------")
        print("1. Xifrar missatge")
        print("2. Desxifrar missatge")
        print("3. Editar rotors")
        print("4. Sortir")
        opcio = input("Selecciona una opcio: ")

        if opcio == '1':
            ut.netejar_pantalla()
            print("XIFRAR MISSATGE")



            configuracio = input("Introdueix la configuracio inicial amb espai entre les lletres: ") #per la configuracio de l'usuari que haura de posar 3 lletres amb espai
            missatge = input("Introdueix el missatge que vulguis xifrar:")
            missatge = missatge.upper() #per posar-ho tota majuscules el missatge
            lletres_valides = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            missatge_buit = "" #es la variable per guardar nomes les lletres i no numeros o caracters especials
            for lletra in missatge:
                if lletra in lletres_valides:
                    missatge_buit += lletra #si es una lletra s'afegeix al missatge 
            
            missatge = missatge_buit
            try:
                missatge_xifrat = xifrar_missatge(missatge,rotor1,rotor2,rotor3,configuracio) #ajuntem totes les variables als parametres de la funcio
                print(f"MISSATGE XIFRAT: {missatge_xifrat}")
                with open ('missatge.txt', 'w') as f:
                 f.write(missatge_xifrat)
            except ValueError:
                print("has posat la configuracio sense espai entre lletres, torna a provar") #per si l'usuari posa la configuracio sense espais que no peti el programa

        elif opcio == '3':
            print("EDITAR ROTORS")
            usuari_rotor = int(input("introdueix quin rotor vols editar: "))
            nom_fitxer = f"data/Rotor{usuari_rotor}.txt"  #aixi ens estalviem haver d'escriure una linea per cada rotor

            
       
        elif  opcio == '4':
            print("has sortit")

main()