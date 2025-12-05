import os

# Aquesta funció neteja la pantalla de la terminal
def netejar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') # Exectuta la comanda de sistema 'cls' si detecta que el sistema es Windows (nt), en cas contrari utilitza 'clear' per sistemes Unix/Linux