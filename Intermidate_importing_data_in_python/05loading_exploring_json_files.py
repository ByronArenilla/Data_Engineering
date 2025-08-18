import json 
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

#Build the json path
j_path = os.path.join(script_dir,'datasets','titanic_parquet.json')

#Load json 
with open(j_path) as json_file:
    json_data = json.load(json_file)
    
#print each key value pair  in jaso_data
for key,value  in json_data.items():
    print(key,':',value)
    