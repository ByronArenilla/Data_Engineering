#Open a file as read-only and bind  it to file
#the file name is prueba.txt
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path to the datasets folder
file_path = os.path.join(script_dir, '..', 'datasets', 'prueba.txt')

with open(file_path, mode = 'r') as file:
    print(file.read())  # Use file.read() to print the content, not the file object