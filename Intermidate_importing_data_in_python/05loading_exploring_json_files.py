import json 
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
j_path = os.path.join(script_dir,'..','datasets','titanic_parquet.json')

print("Ruta del script:", script_dir)
print("Ruta construida:", j_path)
print("Existe?", os.path.exists(j_path))

if os.path.exists(os.path.join(script_dir,'..','datasets')):
    print("Archivos en datasets:", os.listdir(os.path.join(script_dir,'..','datasets')))


datasets_dir = os.path.join(script_dir, '..', 'datasets')
print("Archivos en datasets:", os.listdir(datasets_dir))
