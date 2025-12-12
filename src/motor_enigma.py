import constants as c
import utils as ut

# Mostra el menu principal
def menu_seleccio():
    ut.netejar_pantalla()
    print("\nENIGMA")
    print("--------------")
    print("1. Xifrar missatge")
    print("2. Desxifrar missatge")
    print("3. Editar rotors")
    print("4. Sortir")

# Funcio per carregar el fitxer del rotor
def carregar_fitxer(nom_fitxer): #primer la funcio per llegir les linees del arxiu rotor i les guardi 
    with open(nom_fitxer, 'r') as f:
        contingut = f.readlines()
    cablejat = contingut[0].strip()  #perque la primera l�nea no tingui espais de mes ni res

    if len(contingut) > 1: #en cas de que no hi hagi notch, aquest bloc fa que s'assigni la Z com a notch
        notch = contingut[1].strip()
    else:
        notch = 'Z'
    return {'cablejat': cablejat, 'notch' : notch}

# Funcio per formatar el missatge en grups de cinc lletres
def grups_de_cinc(missatge):
    resultat = ""
    contador = 0
    for lletra in missatge:
        if contador == 5:
            resultat += " "
            contador = 0
        resultat += lletra
        contador += 1
    return resultat

# Funcio per informar sobre el missatge xifrat
def informar_xifrat(missatge_xifrat_raw, missatge_xifrat, ruta_fitxer):
    # Mostra un missatge d'informacio sobre el missatge xifrat
    len_missatge = len(missatge_xifrat_raw)
    grups_5 = len(missatge_xifrat.split())
    print(c.VERD + "[OK] Missatge xifrat a \"{ruta_fitxer}\" ({len_missatge} lletres, {grups_5} grups de 5)" + c.RESET)

# Funcio per treure els accents i caracters especial com la ñ i la ç del missatge
def treure_accents(missatge):
    #Aquesta funcio substitueix les lletres amb accents per les seves equivalents sense accents
    for original, substitucio in c.SUBSTITUCIONS.items():
        missatge = missatge.replace(original, substitucio)
    return missatge

#
def llegir_missatge(nom_fitxer):
    try:
    #Intenta obrir el fitxer i llegir el contingut
        with open(nom_fitxer, 'r') as f:
            missatge = f.read().strip().replace(" ", "")  #Elimina els espais en blanc del missatge
        #Comprova si el missatge esta buit
        if not missatge:
            return(c.VERMELL + "ERROR: el fitxer de missatge esta buit. Torna-ho a intentar." + c.RESET)
        return missatge
    except FileNotFoundError:
        return(c.VERMELL + f"ERROR: No s'ha trobat el fitxer {nom_fitxer}." + c.RESET)
    except PermissionError:
        return(c.VERMELL + f"ERROR: No tens permisos per llegir el fitxer {nom_fitxer}." + c.RESET)
    except Exception as e:
        return(c.VERMELL + f"ERROR inesperat: {e}" + c.RESET)

#Ens permet verificar que la configuracio sigui valida
def validar_configuracio(configuracio):
    # Comprova que la configuracio no estigui buida
    if not configuracio:
        return c.VERMELL + "ERROR: La configuracio no pot estar buida." + c.RESET
    parts = configuracio.upper().split()
    # Comprova que la configuracio contingui exactament tres parts
    if len(parts) != 3:
        return c.VERMELL + "ERROR: La configuracio ha de contenir exactament tres caracters separats per espais." + c.RESET

    posicio1, posicio2, posicio3 = parts
    
    for p in (posicio1, posicio2, posicio3):
        # Comprova que cada posicio estigui a l'alfabet, si no retorna un error
        if len(p) != 1 or p not in c.ALFABET:
            return c.VERMELL + f"ERROR: el caracter '{p}' no es valid" + c.RESET
    
    return posicio1, posicio2, posicio3

# Funcio per xifrar el missatge
def xifrar_missatge(missatge,rotor1,rotor2,rotor3,configuracio):  #es el que es necessita per encendre la maquina
    lletres_xifrades = ""
    posicio1, posicio2, posicio3 = configuracio.split()  #per assignar cada lletra que posi l'usuari a cada rotor
    index1 = c.ALFABET.index(posicio1)  #per convertir les lletres de la configuracio en numeros perque no podem sumar a les lletres per fer girar cada rotor
    index2 = c.ALFABET.index(posicio2) #.index() el que fa es retornar el numero de posicio de la lletra
    index3 = c.ALFABET.index(posicio3)

    for lletra in missatge:
        if c.ALFABET[index1] == rotor1['notch']:#si s'arriba al notch del rotor 1 s'activa el rotor 2 i avança una posicio
            if c.ALFABET[index2] == rotor2['notch']: #abans d'avançar el rotor 2 ha de veure si la posicio de l'index es al notch
                       index3 += 1
                       index3 %= 26
            index2 += 1
            index2 = index2 % 26 #si la posicio arriba a 26 ha de comenzar de nou el rotor 2
        index1 += 1
        index1 %= 26 #quan es passi de les 25 lletres que torni a comenzar
        index_lletra = c.ALFABET.index(lletra)  #guarda la posicio de la lletra qu ha posat l'usuari
        index_entrada = (index_lletra + index1) % c.LEN_ALFABET  #calcula l'entrada real sumant el gir del rotor a la lletra
        lletra_sortida = rotor1['cablejat'][index_entrada] #torna la lletra que hi ha conectada al numero de posicio
        index_sortida = c.ALFABET.index(lletra_sortida) #per passar la lletra al rotor 2 s'ha de passar a numero, que es el seu index de posicio actual
        index_entrada2 = (index_sortida - index1 + index2) % c.LEN_ALFABET
        lletra_sortida2 = rotor2['cablejat'][index_entrada2]
        index_sortida2 = c.ALFABET.index(lletra_sortida2)
        index_entrada3 = (index_sortida2 - index2 + index3) % c.LEN_ALFABET
        lletra_sortida3 = rotor3['cablejat'][index_entrada3]
        index_sortida3 = c.ALFABET.index(lletra_sortida3)
        index_final = (index_sortida3 - index3) % c.LEN_ALFABET
        lletra_final = c.ALFABET[index_final]
        lletres_xifrades += lletra_final
    return lletres_xifrades

# Funcio per desxifrar una lletra en un rotor donat
def desxifrar_lletra(rotor, index_lletra, desplacament):
    index_sortida = (index_lletra + desplacament) % c.LEN_ALFABET #Agafem el residu de la suma de l'index de la lletra i el desplacament dividit per la llargada de l'alfabet
    lletra_sortida = c.ALFABET[index_sortida] #Lletra que correspon a l'index de sortida
    index_entrada = rotor['cablejat'].index(lletra_sortida) #Numero de posicio de lletra_sortida al cablejat del rotor
    return index_entrada

# Funcio per desxifrar el missatge
def desxifrar_missatge(missatge_xifrat, rotor1, rotor2, rotor3, configuracio):
    lletres_desxifrades = ""
    # Passa la configuracio a majuscules i la separa en les posicions inicials dels rotors

    posicio1, posicio2, posicio3 = configuracio

    #INDEX -> Posicio actual de cada rotor
    index1 = c.ALFABET.index(posicio1)
    index2 = c.ALFABET.index(posicio2)
    index3 = c.ALFABET.index(posicio3)

    # Recorrem cada lletra del missatge xifrat i detectem si es troba a l'alfabet
    for lletra in missatge_xifrat:
        if lletra not in c.ALFABET:
            return c.VERMELL + f"ERROR: el caracter '{lletra}' del missatge xifrat no esta a l'alfabet" + c.RESET

        if c.ALFABET[index1] == rotor1['notch']:
            if c.ALFABET[index2] == rotor2['notch']:
                index3 = (index3 + 1) % c.LEN_ALFABET
            index2 = (index2 + 1) % c.LEN_ALFABET
        index1 = (index1 + 1) % c.LEN_ALFABET

        # PER DESXIFRAR

        #Rotor 3
        index_lletra = c.ALFABET.index(lletra) #Numero de posicio a l'alfabet
        index_entrada3 = desxifrar_lletra(rotor3, index_lletra, index3)

        #Rotor 2
        index_entrada2 = desxifrar_lletra(rotor2, index_entrada3, index2 - index3)
        
        #Rotor 1
        index_entrada1 = desxifrar_lletra(rotor1, index_entrada2, index1 - index2)

        #Lletra desxifrada
        index_final = (index_entrada1 - index1) % c.LEN_ALFABET 
        lletra_desxifrada = c.ALFABET[index_final]
        lletres_desxifrades += lletra_desxifrada
    return lletres_desxifrades

# Guarda el missatge desxifrat en un fitxer
def guardar_missatge(ruta_fitxer, missatge):
    try:
        with open(ruta_fitxer, 'w') as f:
            f.write(missatge)
    except PermissionError:
        return c.VERMELL + f"ERROR: No tens permisos per escriure al {ruta_fitxer}." + c.RESET
    except Exception as e:
        return c.VERMELL + f"ERROR: S'ha produit un error inesperat en escriure al {ruta_fitxer}: {e}" + c.RESET
   
# Neteja el missatge eliminant caracters especials i numeros
def netejar_missatge(missatge):
    missatge_buit = "" #es la variable per guardar nomes les lletres i no numeros o caracters especials
    for lletra in missatge:
        if lletra in c.ALFABET:
            missatge_buit += lletra #si es una lletra s'afegeix al missatge 
        else:
            print(c.GROC + f"El caracter {lletra} s'ha omes ja que no esta a l'abecedari" + c.RESET)
    return missatge_buit

#Es la funcio per comprovar si hi han lletres repetides al nou cablejat
def check_lletres_repetides(cablejat_nou):
    for i in range(len(cablejat_nou)):
        for j in range(i + 1, len(cablejat_nou)):
            if cablejat_nou[i] == cablejat_nou[j]:
                return True #ordenem amb bubble sort per veure si hi han lletres repetides i si hi ha es torna True
    return False

# Funcio principal per al xifratge del missatge
def process_xifratge(rotor1, rotor2, rotor3):
    ut.netejar_pantalla()
    print("XIFRAR MISSATGE")
    configuracio = input("Introdueix la configuracio inicial amb espai entre les lletres: ") #per la configuracio de l'usuari que haura de posar 3 lletres amb espai

    resposta = validar_configuracio(configuracio) #cridem la funcio per validar la configuracio
    if "ERROR" in resposta:
        print(resposta)  #si hi ha un error el mostrem
        input("\nPremeu qualsevol tecla per a continuar. . .")
        return  #torna al menu principal

    posicio1, posicio2, posicio3 = resposta
    configuracio = f"{posicio1} {posicio2} {posicio3}"

    missatge = input("Introdueix el missatge que vulguis xifrar:").upper().replace(" ", "") #per posar-ho tota majuscules el missatge
    missatge = treure_accents(missatge)
    missatge = netejar_missatge(missatge) #eliminem els caracters especials i numeros del missatge

    print(f"Missatge netejat: {missatge}") #mostrem el missatge netejat per a que l'usuari vegi com ha quedat

    missatge_xifrat_raw = xifrar_missatge(missatge,rotor1,rotor2,rotor3,configuracio) #ajuntem totes les variables als parametres de la funcio
    missatge_xifrat = grups_de_cinc(missatge_xifrat_raw) #per formatar el missatge en grups de cinc

    print(f"MISSATGE XIFRAT: {missatge_xifrat}")
    error_guardar = guardar_missatge(c.RUTA_MISSATGE, missatge_xifrat)

    if error_guardar:
        print(error_guardar)
        input("\nPremeu qualsevol tecla per a continuar. . .")
        return

    informar_xifrat(missatge_xifrat_raw, missatge_xifrat, c.RUTA_MISSATGE)
    input("\nPremeu qualsevol tecla per a continuar. . .")

# Funcio principal per al desxifratge del missatge
def process_desxifratge(rotor1, rotor2, rotor3):
    ut.netejar_pantalla()
    print("DESXIFRAR MISSATGE")
    configuracio = input("Introdueix la configuracio inicial amb espai entre les lletres: ")
    resposta = validar_configuracio(configuracio) #cridem la funcio per validar la configuracio
    if "ERROR" in resposta:
        print(resposta)  #si hi ha un error el mostrem
        input("\nPremeu qualsevol tecla per a continuar. . .")
        return  #torna al menu principal
    missatge = llegir_missatge(c.RUTA_MISSATGE)
    if "ERROR" in missatge:
        print(missatge)
        input("\nPremeu qualsevol tecla per a continuar. . .")
        return
    print(f"Missatge xifrat llegit des del fitxer: {missatge}")
    #Netejem el missatge llegit del fitxer per assegurar-nos que no hi ha caracters especials ni espais
    missatge = missatge.replace(" ", "")  #eliminem els espais del missatge llegit del fitxer
    missatge = treure_accents(missatge)
    missatge = netejar_missatge(missatge) #eliminem els caracters especials i numeros del missatge
    print(f"Missatge netejat: {missatge}") #mostrem el missatge netejat per a que l'usuari vegi com ha quedat
    missatge_desxifrat = desxifrar_missatge(missatge, rotor1, rotor2, rotor3, resposta)
    #Ens permet controlar els errors produits durant el desxifratge
    if "ERROR" in missatge_desxifrat:
        print(missatge_desxifrat)
        input("\nPremeu qualsevol tecla per a continuar. . .")
        return
    error_guardar = guardar_missatge(c.RUTA_MISSATGE_DESXIFRAT, missatge_desxifrat)
    if error_guardar:
        print(error_guardar)
        input("\nPremeu qualsevol tecla per a continuar. . .")
        return
    print(missatge_desxifrat) #Si tot funciona, mostra el missatge desxifrat
    input("\nPremeu qualsevol tecla per a continuar. . .")

# Funcio per demanar a l'usuari quin rotor vol editar
def numero_rotor():
    num = input("Introdueix quin rotor vols editar (1-3): ")
    if num.isdigit():
        num = int(num)
        if num in (1, 2, 3):
            return num
    return ""

def process_editar_rotor():
    ut.netejar_pantalla()
    print("EDITAR ROTORS")
    usuari_rotor = numero_rotor()
    if not usuari_rotor:
        print(c.VERMELL + "ERROR: Numero de rotor no valid. Ha de ser 1, 2 o 3" + c.RESET)
        input("\nPremeu qualsevol tecla per a continuar. . .")
        return  #torna al principi del bucle si hi ha un error

    nom_fitxer = f"data/Rotor{usuari_rotor}.txt"  #aixi ens estalviem haver d'escriure una linea per cada rotor
    cablejat_nou = input("Introdueix el nou cablejat de 26 lletres: ").upper() #demanem el nou cablejat que vol l'usuari
    notch_nou = input("Introdueix el nou notch (deixa buit per defecte 'Z'): ").upper()
    if len(cablejat_nou) != c.LEN_ALFABET:
        print(c.VERMELL + "ERRORHa de tindre exactament 26 lletres" + c.RESET)
        input("\nPremeu qualsevol tecla per a continuar. . .")
        return  #si no es posen les 26 linies ha de tornar al principi del bucle 
    if check_lletres_repetides(cablejat_nou):
        print(c.VERMELL + "ERROR: Hi ha lletres repetides, torna a provar" + c.RESET)
        input("\nPremeu qualsevol tecla per a continuar. . .")
        return
    if notch_nou == '' or notch_nou not in c.ALFABET or len(notch_nou) != 1:
        notch_nou = 'Z' #es el valor per defecte que li posem al notch si el fitxer esta buit

    contingut = cablejat_nou + "\n" + notch_nou
    error_guardar = guardar_missatge(nom_fitxer, contingut)

    if error_guardar: # SI HI HA ALGO DINS DE error_guardar significa que hi ha hagut un error, ja que la funcio no retorna res si ha funcionat
        print(error_guardar)
        input("\nPremeu qualsevol tecla per a continuar. . .")
        return
    else:
        print(c.VERD + "El rotor s'ha acualitzat" + c.RESET)
    input("\nPremeu qualsevol tecla per a continuar. . .")