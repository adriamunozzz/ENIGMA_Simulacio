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
                with open ('data/missatge.txt', 'w') as f:
                 f.write(missatge_xifrat)
            except ValueError:
                print("has posat la configuracio sense espai entre lletres, torna a provar") #per si l'usuari posa la configuracio sense espais que no peti el programa

        elif opcio == '3':
            print("EDITAR ROTORS")
            usuari_rotor = int(input("introdueix quin rotor vols editar: "))
            nom_fitxer = f"data/Rotor{usuari_rotor}.txt"  #aixi ens estalviem haver d'escriure una linea per cada rotor
            cablejat_nou = input("introdueix el nou cablejat de 26 lletres: ").upper() #demanem el nou cablejat que vol l'usuari
            if len(cablejat_nou) != 26:
                print("ha de tindre exactament 26 lletres")
                continue  #si no es posen les 26 linies ha de tornar al principi del bucle 

            lletres_repetides = False #al principi no te lletres repetides
            for i in range(len(cablejat_nou)):
                for j in range(i + 1, len(cablejat_nou)):
                    if cablejat_nou[i] == cablejat_nou[j]:
                        lletres_repetides = True #ordenem amb bubble sort per veure si hi han lletres repetides i si hi ha es torna True
                        break
                if lletres_repetides:
                     break

            if lletres_repetides:
                print("hi ha lletres repetides, torna a provar")
            else:
                notch_nou = 'Z' #es el valor per defecte que li posem al notch si el fitxer esta buit
                try:
                    with open(nom_fitxer, 'r') as f:
                        linies = f.readlines() #per llegir les linies que te el fitxer actualment
                        if len(linies) > 1:
                            notch_nou = linies[1] #aixo es si existeix el notch  li posem a la variable
                except ValueError:
                    pass #el control d'errors perque si hi ha algun error el nou notch del rotor sigui la Z 

                with open(nom_fitxer, 'w') as f:
                    f.write(cablejat_nou + "\n") #el nou cablejat de l'usuari
                    f.write(notch_nou) #el notch que hi havia
                print("el rotor ja s'ha acualitzat")

                if usuari_rotor == 1: rotor1 = carregar_fitxer(nom_fitxer)
                if usuari_rotor == 2: rotor2 = carregar_fitxer(nom_fitxer)
                if usuari_rotor == 3: rotor3 = carregar_fitxer(nom_fitxer)



            
       
        elif  opcio == '4':
            print("has sortit")

main()
