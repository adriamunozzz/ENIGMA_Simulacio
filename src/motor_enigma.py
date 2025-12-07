import constants as c

def carregar_fitxer(nom_fitxer): #primer la funcio per llegir les linees del arxiu rotor i les guardi 
    with open(nom_fitxer, 'r') as f:
        contingut = f.readlines()
    cablejat = contingut[0].strip()  #perque la primera l�nea no tingui espais de mes ni res

    if len(contingut) > 1: #en cas de que no hi hagi notch, aquest bloc fa que s'assigni la Z com a notch
        notch = contingut[1].strip()
    else:
        notch = 'Z'
    return {'cablejat': cablejat, 'notch' : notch}

def llegir_missatge(nom_fitxer):
    try:
    #Intenta obrir el fitxer i llegir el contingut
        with open(nom_fitxer, 'r') as f:
            missatge = f.read().strip().replace(" ", "")  #Elimina els espais en blanc del missatge
        #Comprova si el missatge esta buit
        if not missatge:
            return("ERROR: el fitxer de missatge esta buit. Torna-ho a intentar.")
        return missatge
    except FileNotFoundError:
        return f"ERROR: No s'ha trobat el fitxer {nom_fitxer}."
    except PermissionError:
        return f"ERROR: No tens permisos per llegir el fitxer {nom_fitxer}."
    except Exception as e:
        return f"ERROR inesperat: {e}"

#Ens permet verificar que la configuracio sigui valida
def validar_configuracio(configuracio):
    # Passa la configuracio a majuscules i la separa en les posicions inicials dels rotors
    try:
        posicio1, posicio2, posicio3 = configuracio.upper().split()
    except ValueError:
        return "ERROR: La configuracio ha de contenir exactament tres caracters separats per espais."
    
    for p in (posicio1, posicio2, posicio3):
        # Comprova que cada posicio estigui a l'alfabet, si no retorna un error
        if p not in c.ALFABET:
            return f"ERROR: el caracter '{p}' no esta a l'alfabet"
    
    return posicio1, posicio2, posicio3

def xifrar_missatge(missatge,rotor1,rotor2,rotor3,configuracio):  #es el que es necessita per encendre la maquina
    lletres_xifrades = ""
    posicio1, posicio2, posicio3 = configuracio.split()  #per assignar cada lletra que posi l'usuari a cada rotor
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index1 = alfabet.index(posicio1)  #per convertir les lletres de la configuracio en numeros perque no podem sumar a les lletres per fer girar cada rotor
    index2 = alfabet.index(posicio2) #.index() el que fa es retornar el numero de posicio de la lletra
    index3 = alfabet.index(posicio3)

    for lletra in missatge:
        if alfabet[index1] == rotor1['notch']:#si s'arriba al notch del rotor 1 s'activa el rotor 2 i avança una posicio
            if alfabet[index2] == rotor2['notch']: #abans d'avançar el rotor 2 ha de veure si la posicio de l'index es al notch
                       index3 += 1
                       index3 %= 26
            index2 += 1
            index2 = index2 % 26 #si la posicio arriba a 26 ha de comenzar de nou el rotor 2
        index1 += 1
        index1 %= 26 #quan es passi de les 25 lletres que torni a comenzar
        index_lletra = alfabet.index(lletra)  #guarda la posicio de la lletra qu ha posat l'usuari
        index_entrada = (index_lletra + index1) % 26  #calcula l'entrada real sumant el gir del rotor a la lletra
        lletra_sortida = rotor1['cablejat'][index_entrada] #torna la lletra que hi ha conectada al numero de posicio
        index_sortida = alfabet.index(lletra_sortida) #per passar la lletra al rotor 2 s'ha de passar a numero, que es el seu index de posicio actual
        index_entrada2 = (index_sortida - index1 + index2) % 26
        lletra_sortida2 = rotor2['cablejat'][index_entrada2]
        index_sortida2 = alfabet.index(lletra_sortida2)
        index_entrada3 = (index_sortida2 - index2 + index3) % 26
        lletra_sortida3 = rotor3['cablejat'][index_entrada3]
        index_sortida3 = alfabet.index(lletra_sortida3)
        index_final = (index_sortida3 - index3) % 26
        lletra_final = alfabet[index_final]
        lletres_xifrades += lletra_final
    return lletres_xifrades

def desxifrar_lletra(rotor, index_lletra, desplacament):
    index_sortida = (index_lletra + desplacament) % c.LEN_ALFABET #Agafem el residu de la suma de l'index de la lletra i el desplacament dividit per la llargada de l'alfabet
    lletra_sortida = c.ALFABET[index_sortida] #Lletra que correspon a l'index de sortida
    index_entrada = rotor['cablejat'].index(lletra_sortida) #Numero de posicio de lletra_sortida al cablejat del rotor
    return index_entrada

def desxifrar_missatge(missatge_xifrat, rotor1, rotor2, rotor3, configuracio):
    lletres_desxifrades = ""
    # Passa la configuracio a majuscules i la separa en les posicions inicials dels rotors

    resposta = validar_configuracio(configuracio)
    if "ERROR" in resposta:
        return resposta

    posicio1, posicio2, posicio3 = resposta

    #INDEX -> Posicio actual de cada rotor
    index1 = c.ALFABET.index(posicio1)
    index2 = c.ALFABET.index(posicio2)
    index3 = c.ALFABET.index(posicio3)

    # Recorrem cada lletra del missatge xifrat i detectem si es troba a l'alfabet
    for lletra in missatge_xifrat:
        if lletra not in c.ALFABET:
            return f"ERROR: el caracter '{lletra}' del missatge xifrat no esta a l'alfabet"

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
        return f"ERROR: No tens permisos per escriure el fitxer de missatge desxifrat."
    except Exception as e:
        return f"ERROR: S'ha produit un error inesperat en escriure el fitxer: {e}"


rotor1 = carregar_fitxer('data/Rotor1.txt')
rotor2 = carregar_fitxer('data/Rotor2.txt')
rotor3 = carregar_fitxer('data/Rotor3.txt')


# configuracio = input("escriu la configuracio inicial: ")
# missatge = input("escriu el missatge que vols xifrar: ")

# resultat = xifrar_missatge(missatge, rotor1, rotor2, rotor3, configuracio)
# print("missatge xifrat: ", resultat)
