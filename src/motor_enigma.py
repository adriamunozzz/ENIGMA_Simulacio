def carregar_fitxer(nom_fitxer): #primer la funcio per llegir les linees del arxiu rotor i les guardi 
    with open(nom_fitxer, 'r') as f:
        contingut = f.readlines()
    cablejat = contingut[0].strip()  #perque la primera línea no tingui espais de mes ni res

    if len(contingut) > 1: #en cas de que no hi hagi notch, aquest bloc fa que s'assigni la Z com a notch
        notch = contingut[1].strip()
    else:
        notch = 'Z'
    return {'cableado': cablejat, 'notch' : notch}