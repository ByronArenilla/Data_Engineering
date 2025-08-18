import requests

#Assing the url to the variable url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

#package the request, send the request and catch the response
r = requests.get(url)

#Decode the json data into a dictionary
json_data = r.json()

# print each key value
for k in json_data.keys():
    print(k+': ',json_data[k])