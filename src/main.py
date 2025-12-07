from motor_enigma import carregar_fitxer, informar_xifrat, xifrar_missatge, desxifrar_missatge, guardar_missatge, llegir_missatge, validar_configuracio, grups_de_cinc
import utils as ut
#LLIBRERIA DE CONSTANTS
import constants as c
def main():
    rotor1 = carregar_fitxer(c.RUTA_ROTOR1) #afegim com a variable cada rotor per si l'usuari escogeix l'opcio de editar rotors
    rotor2 = carregar_fitxer(c.RUTA_ROTOR2) #aixi un coop torni a sortir el menu tindra les dades actulitzades
    rotor3 = carregar_fitxer(c.RUTA_ROTOR3)

    opcio = '0'
    while opcio != '4':

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
            configuracio = input("Introdueix la configuracio inicial amb espai entre les lletres: ") #per la configuracio de l'usuari que haura de posar 3 lletres amb espai

            resposta = validar_configuracio(configuracio) #cridem la funcio per validar la configuracio
            if "ERROR" in resposta:
                print(resposta)  #si hi ha un error el mostrem
                input("\nPremeu qualsevol tecla per a continuar. . .")
                continue  #torna al principi del bucle

            posicio1, posicio2, posicio3 = resposta
            configuracio = f"{posicio1} {posicio2} {posicio3}"

            missatge = input("Introdueix el missatge que vulguis xifrar:").upper().replace(" ", "") #per posar-ho tota majuscules el missatge
            lletres_valides = c.ALFABET
            missatge_buit = "" #es la variable per guardar nomes les lletres i no numeros o caracters especials
            for lletra in missatge:
                if lletra in lletres_valides:
                    missatge_buit += lletra #si es una lletra s'afegeix al missatge 
            
            missatge = missatge_buit
            try:
                missatge_xifrat_raw = xifrar_missatge(missatge,rotor1,rotor2,rotor3,configuracio) #ajuntem totes les variables als parametres de la funcio
                missatge_xifrat = grups_de_cinc(missatge_xifrat_raw) #per formatar el missatge en grups de cinc
                print(f"MISSATGE XIFRAT: {missatge_xifrat}")
                with open (c.RUTA_MISSATGE, 'w') as f:
                    f.write(missatge_xifrat)
                informar_xifrat(missatge_xifrat_raw, missatge_xifrat, c.RUTA_MISSATGE)
            except ValueError:
                print("ERROR: has posat la configuracio sense espai entre lletres, torna a provar") #per si l'usuari posa la configuracio sense espais que no peti el programa

            input("\nPremeu qualsevol tecla per a continuar. . .")
        elif opcio == '2':
            ut.netejar_pantalla()
            print("DESXIFRAR MISSATGE")
            configuracio = input("Introdueix la configuracio inicial: ")

            # Aquesta condicio ens assegura que la configuracio sigui valida, si no ho es torna al menu principal
            if not configuracio or len(configuracio.split()) != 3:
                print("Configuracio no valida. Torna-ho a intentar.")
                input("\nPremeu qualsevol tecla per a continuar. . .")
                continue

            missatge = llegir_missatge(c.RUTA_MISSATGE)
            if "ERROR" in missatge:
                print(missatge)
                input("\nPremeu qualsevol tecla per a continuar. . .")
                continue
            
            print(f"Missatge xifrat llegit des del fitxer: {missatge}")

            missatge_desxifrat = desxifrar_missatge(missatge, rotor1, rotor2, rotor3, configuracio)
            #Ens permet controlar els errors produits durant el desxifratge
            if "ERROR" in missatge_desxifrat:
                print(missatge_desxifrat)
                input("\npremeu qualsevol tecla per a continuar. . .")
                continue

            error_guardar = guardar_missatge(c.RUTA_MISSATGE_DESXIFRAT, missatge_desxifrat)
            if error_guardar:
                print(error_guardar)
                input("\nPremeu qualsevol tecla per a continuar. . .")
                continue
            #Si tot funciona, mostra el missatge desxifrat
            print(missatge_desxifrat)
            input("\nPremeu qualsevol tecla per a continuar. . .")      
        elif opcio == '3':
            print("EDITAR ROTORS")
            usuari_rotor = int(input("introdueix quin rotor vols editar: "))
            nom_fitxer = f"data/Rotor{usuari_rotor}.txt"  #aixi ens estalviem haver d'escriure una linea per cada rotor
            cablejat_nou = input("introdueix el nou cablejat de 26 lletres: ").upper() #demanem el nou cablejat que vol l'usuari
            if len(cablejat_nou) != c.LEN_ALFABET:
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
            input("\nPremeu qualsevol tecla per a continuar. . .")
        elif opcio == '4':
            print("Has sortit")

main()
