#importando os
import os
#Obteniendo la ruta del script donde estoy trabajando
script_path = os.path.dirname(os.path.abspath(__file__))
#construyedo la ruta para acceder al txt
file_path = os.path.join(script_path,'..','datasets','quijote.txt')

with open(file_path, mode = 'r') as file:
    print(file.read())