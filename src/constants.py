ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LEN_ALFABET = 26
RUTA_ROTOR1 = "data/Rotor1.txt"
RUTA_ROTOR2 = "data/Rotor2.txt"
RUTA_ROTOR3 = "data/Rotor3.txt"
RUTA_MISSATGE = "data/missatge.txt"
RUTA_MISSATGE_DESXIFRAT = "output/desxifrat.txt"

#COLORS PER LA TERMINAL
VERMELL = "\033[31m"
VERD    = "\033[32m"
GROC    = "\033[33m"
RESET   = "\033[0m"

#DICCIONARI DE SUBSTITUCIONS PER NETEJAR MISSATGE
SUBSTITUCIONS = {
    #A
    "á": "a", "à": "a", "ä": "a", "â": "a",
    "Á": "A", "À": "A", "Ä": "A", "Â": "A",
    #E
    "é": "e", "è": "e", "ë": "e", "ê": "e",
    "É": "E", "È": "E", "Ë": "E", "Ê": "E",
    #I
    "í": "i", "ì": "i", "ï": "i", "î": "i",
    "Í": "I", "Ì": "I", "Ï": "I", "Î": "I",
    #O
    "ó": "o", "ò": "o", "ö": "o", "ô": "o",
    "Ó": "O", "Ò": "O", "Ö": "O", "Ô": "O",
    #U
    "ú": "u", "ù": "u", "ü": "u", "û": "u",
    "Ú": "U", "Ù": "U", "Ü": "U", "Û": "U",
    #C, N
    "ç": "c", "Ç": "C", "ñ": "n", "Ñ": "N",
    "·":""
}