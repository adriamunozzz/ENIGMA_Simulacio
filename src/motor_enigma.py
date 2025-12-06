def carregar_fitxer(nom_fitxer): #primer la funcio per llegir les linees del arxiu rotor i les guardi 
    with open(nom_fitxer, 'r') as f:
        contingut = f.readlines()
    cablejat = contingut[0].strip()  #perque la primera l�nea no tingui espais de mes ni res

    if len(contingut) > 1: #en cas de que no hi hagi notch, aquest bloc fa que s'assigni la Z com a notch
        notch = contingut[1].strip()
    else:
        notch = 'Z'
    return {'cablejat': cablejat, 'notch' : notch}  #diu el cablejat i el notch del rotor que s'escogeixi

def xifrar_missatge(missatge,rotor1,rotor2,rotor3,configuracio):  #es el que es necessita per encendre la maquina
    lletres_xifrades = ""
    posicio1, posicio2, posicio3 = configuracio.split()  #per assignar cada lletra que posi l'usuari a cada rotor
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index1 = alfabet.index(posicio1)  #per convertir les lletres de la configuracio en numeros perque no podem sumar a les lletres per fer girar cada rotor
    index2 = alfabet.index(posicio2) #.index() el que fa es retornar el numero de posicio de la lletra
    index3 = alfabet.index(posicio3)

    for lletra in missatge:
        if alfabet[index1] == rotor1['notch']:#si s'arriba al notch del rotor 1 s'activa el rotor 2 i avan�a una posicio
            if alfabet[index2] == rotor2['notch']: #abans d'avan�ar el rotor 2 ha de veure si la posicio de l'index es al notch
                       index3 += 1
                       index3 %= 26
            index2 += 1
            index2 = index2 % 26 #si la posicio arriba a 26 ha de comen�ar de nou el rotor 2
        index1 += 1
        index1 %= 26 #quan es passi de les 25 lletres que torni a comen�ar
        index_lletra = alfabet.index(lletra)  #guarda la posicio de la lletra qu ha posat l'usuari
        index_entrada = (index_lletra + index1) % 26  #calcula l�entrada real sumant el gir del rotor a la lletra
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



rotor1 = carregar_fitxer('data/Rotor1.txt')
rotor2 = carregar_fitxer('data/Rotor2.txt')
rotor3 = carregar_fitxer('data/Rotor3.txt')


# configuracio = input("escriu la configuracio inicial: ")
# missatge = input("escriu el missatge que vols xifrar: ")

# resultat = xifrar_missatge(missatge, rotor1, rotor2, rotor3, configuracio)
# print("missatge xifrat: ", resultat)
