import motor_enigma as enigma
import utils as ut
import constants as c #LLIBRERIA DE CONSTANTS
def main():
    rotor1 = enigma.carregar_fitxer(c.RUTA_ROTOR1) #afegim com a variable cada rotor per si l'usuari escogeix l'opcio de editar rotors
    rotor2 = enigma.carregar_fitxer(c.RUTA_ROTOR2) #aixi un coop torni a sortir el menu tindra les dades actulitzades
    rotor3 = enigma.carregar_fitxer(c.RUTA_ROTOR3)

    opcio = '0'
    while opcio != '4':
        enigma.menu_seleccio()
        opcio = input("Selecciona una opcio: ")

        if opcio == '1':
            ut.netejar_pantalla()
            print("XIFRAR MISSATGE")
            configuracio = input("Introdueix la configuracio inicial amb espai entre les lletres: ") #per la configuracio de l'usuari que haura de posar 3 lletres amb espai

            resposta = enigma.validar_configuracio(configuracio) #cridem la funcio per validar la configuracio
            if "ERROR" in resposta:
                print(resposta)  #si hi ha un error el mostrem
                input("\nPremeu qualsevol tecla per a continuar. . .")
                continue  #torna al principi del bucle

            posicio1, posicio2, posicio3 = resposta
            configuracio = f"{posicio1} {posicio2} {posicio3}"

            missatge = input("Introdueix el missatge que vulguis xifrar:").upper().replace(" ", "") #per posar-ho tota majuscules el missatge
            missatge = enigma.netejar_missatge(missatge) #eliminem els caracters especials i numeros del missatge

            try:
                missatge_xifrat_raw = enigma.xifrar_missatge(missatge,rotor1,rotor2,rotor3,configuracio) #ajuntem totes les variables als parametres de la funcio
                missatge_xifrat = enigma.grups_de_cinc(missatge_xifrat_raw) #per formatar el missatge en grups de cinc
                print(f"MISSATGE XIFRAT: {missatge_xifrat}")
                with open (c.RUTA_MISSATGE, 'w') as f:
                    f.write(missatge_xifrat)
                enigma.informar_xifrat(missatge_xifrat_raw, missatge_xifrat, c.RUTA_MISSATGE)
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

            missatge = enigma.llegir_missatge(c.RUTA_MISSATGE)
            if "ERROR" in missatge:
                print(missatge)
                input("\nPremeu qualsevol tecla per a continuar. . .")
                continue
            
            print(f"Missatge xifrat llegit des del fitxer: {missatge}")

            missatge_desxifrat = enigma.desxifrar_missatge(missatge, rotor1, rotor2, rotor3, configuracio)
            #Ens permet controlar els errors produits durant el desxifratge
            if "ERROR" in missatge_desxifrat:
                print(missatge_desxifrat)
                input("\npremeu qualsevol tecla per a continuar. . .")
                continue

            error_guardar = enigma.guardar_missatge(c.RUTA_MISSATGE_DESXIFRAT, missatge_desxifrat)
            if error_guardar:
                print(error_guardar)
                input("\nPremeu qualsevol tecla per a continuar. . .")
                continue

            print(missatge_desxifrat) #Si tot funciona, mostra el missatge desxifrat
            input("\nPremeu qualsevol tecla per a continuar. . .")      
        elif opcio == '3':
            print("EDITAR ROTORS")
            usuari_rotor = int(input("Introdueix quin rotor vols editar: "))
            nom_fitxer = f"data/Rotor{usuari_rotor}.txt"  #aixi ens estalviem haver d'escriure una linea per cada rotor
            cablejat_nou = input("Introdueix el nou cablejat de 26 lletres: ").upper() #demanem el nou cablejat que vol l'usuari
            if len(cablejat_nou) != c.LEN_ALFABET:
                print("Ha de tindre exactament 26 lletres")
                continue  #si no es posen les 26 linies ha de tornar al principi del bucle 
            elif enigma.check_lletres_repetides(cablejat_nou):
                print("Hi ha lletres repetides, torna a provar")
            else:
                notch_nou = 'Z' #es el valor per defecte que li posem al notch si el fitxer esta buit
                try:
                    with open(nom_fitxer, 'r') as f:
                        linies = f.readlines() #per llegir les linies que te el fitxer actualment
                        if len(linies) > 1:
                            notch_nou = linies[1] #aixo es si existeix el notch  li posem a la variable
                except FileNotFoundError:
                    return f"ERROR: No s'ha trobat el fitxer {nom_fitxer}."
                except PermissionError:
                    return f"ERROR: No tens permisos per llegir el fitxer {nom_fitxer}."
                except Exception as e:
                    return f"ERROR inesperat: {e}" #el control d'errors perque si hi ha algun error el nou notch del rotor sigui la Z

                contingut = cablejat_nou + "\n" + notch_nou
                error_guardar = enigma.guardar_missatge(nom_fitxer, contingut)

                if error_guardar: # SI HI HA ALGO DINS DE error_guardar significa que hi ha hagut un error, ja que la funcio no retorna res si ha funcionat
                    print(error_guardar)
                else:
                    print("El rotor ja s'ha acualitzat")
                    if usuari_rotor == 1: rotor1 = enigma.carregar_fitxer(nom_fitxer)
                    elif usuari_rotor == 2: rotor2 = enigma.carregar_fitxer(nom_fitxer)
                    elif usuari_rotor == 3: rotor3 = enigma.carregar_fitxer(nom_fitxer)
            input("\nPremeu qualsevol tecla per a continuar. . .")
        elif opcio == '4':
            input("Has sortit")
main()