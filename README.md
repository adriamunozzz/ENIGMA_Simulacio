
# ENIGMA - Simulació

Simulació en Python del funcionament bàsic de la màquina ENIGMA, una màquina de xifratge utilitzada durant la Segona Guerra Mundial.
Aquest projecte permet:

- Xifrar missatges
- Desxifrar missatges
- Editar la configuració dels rotors

Treballar amb fitxers de configuració per als rotors i el missatge

L’objectiu és entendre el funcionament dels rotors i del procés de substitució característic de l’ENIGMA.

## Estructura del projecte:
```
ENIGMA_Simulacio/
│
├── data/                 # Fitxers de configuració
│   ├── Missatge.txt
│   ├── Rotor1.txt
│   ├── Rotor2.txt
│   └── Rotor3.txt
│
├── output/               # Fitxers de sortida generats
│
├── src/                  # Codi font del projecte
│   ├── main.py           # Punt d'entrada del programa (menú)
│   ├── motor_enigma.py   # Funcions del motor ENIGMA
│   └── utils.py          # Funcions auxiliars (netejar pantalla, etc.)
│
├── ENIGMA_Simulacio.slnx # Solució per Visual Studio
├── .gitignore
└── README.md
```
## Com executar el projecte a Visual Studio:
1. Clonar repositori
```bash
git clone https://github.com/adriamunozzz/ENIGMA_Simulacio.git
```
2. Obrir el projecte
    1. Obre la carpeta on hagis descarregat el repositori
    2. Fes doble clic a:
    ```
    ENIGMA_Simulacio.slnx
    ```
2. Executar el programa
    1. Prem **F5**
    
## Autors del projecte:
- [Adrià Muñoz](https://github.com/adriamunozzz)
- [Albert Rodriguez](https://github.com/albertrp05)
