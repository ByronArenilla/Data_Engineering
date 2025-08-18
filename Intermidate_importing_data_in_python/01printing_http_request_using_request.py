#import package
import requests

#specify the url 
url = "http://www.datacamp.com/teach/documentation"

#package the request, send the request and catch the response
r = requests.get(url)

#text the request
text = r.text

#Print the request
print(text)