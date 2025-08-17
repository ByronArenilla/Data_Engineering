import os
script_dir = os.path.dirname(os.path.abspath(__file__))
script_file = os.path.join(script_dir,'..','datasets','prueba.txt')
with open(script_file, mode = 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())