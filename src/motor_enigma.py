import constants as c

def carregar_fitxer(nom_fitxer): #primer la funcio per llegir les linees del arxiu rotor i les guardi 
    with open(nom_fitxer, 'r') as f:
        contingut = f.readlines()
    cablejat = contingut[0].strip()  #perque la primera línea no tingui espais de mes ni res

    if len(contingut) > 1: #en cas de que no hi hagi notch, aquest bloc fa que s'assigni la Z com a notch
        notch = contingut[1].strip()
    else:
        notch = 'Z'
    return {'cablejat': cablejat, 'notch' : notch}

def desxifrar_missatge(missatge_xifrat, rotor1, rotor2, rotor3, configuracio):
    lletres_desxifrades = ""
    posicio1, posicio2, posicio3 = configuracio.split()
    # INDEX -> Posicio actual de cada rotor
    index1 = c.alfabet.index(posicio1)
    index2 = c.alfabet.index(posicio2)
    index3 = c.alfabet.index(posicio3)

    for lletra in missatge_xifrat:
        if c.alfabet[index1] == rotor1['notch']:
            if c.alfabet[index2] == rotor2['notch']:
                index3 = (index3 + 1) % 26
            index2 = (index2 + 1) % 26
        index1 = (index1 + 1) % 26
        # PER DESXIFRAR
        #Rotor 3
        index_lletra = c.alfabet.index(lletra)
        index_sortida3 = (index_lletra + index3) % 26
        lletra_sortida3 = c.alfabet[index_sortida3]
        index_entrada3 = rotor3['cablejat'].index(lletra_sortida3) 

        #Rotor 2
        index_sortida2 = (index_entrada3 + index2 - index3) % 26
        lletra_sortida2 = c.alfabet[index_sortida2]
        index_entrada2 = rotor2['cablejat'].index(lletra_sortida2)
        #Rotor 1
        index_sortida1 = (index_entrada2 + index1 - index2) % 26
        lletra_sortida1 = c.alfabet[index_sortida1]
        index_entrada1 = rotor1['cablejat'].index(lletra_sortida1)
        #Lletra desxifrada
        index_final = (index_entrada1 - index1) % 26
    
        lletra_desxifrada = c.alfabet[index_final]
        lletres_desxifrades += lletra_desxifrada
        with open(c.RUTA_MISSATGE_DESXIFRAT, 'w') as f:
            f.write(lletres_desxifrades)
    return lletres_desxifrades