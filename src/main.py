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
            enigma.process_xifratge(rotor1, rotor2, rotor3)
        elif opcio == '2':
            enigma.process_desxifratge(rotor1, rotor2, rotor3)
        elif opcio == '3':
            enigma.process_editar_rotor()
            #Recarreguem els rotors per si s'han fet canvis
            rotor1 = enigma.carregar_fitxer(c.RUTA_ROTOR1)
            rotor2 = enigma.carregar_fitxer(c.RUTA_ROTOR2)
            rotor3 = enigma.carregar_fitxer(c.RUTA_ROTOR3)
        elif opcio == '4':
            ut.netejar_pantalla()
            input("Has sortit\nPremeu qualsevol tecla per a continuar. . .")
main()