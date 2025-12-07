from motor_enigma import carregar_fitxer, desxifrar_missatge, guardar_missatge, llegir_missatge
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

        elif opcio == '4':
            print("Has sortit")

main()