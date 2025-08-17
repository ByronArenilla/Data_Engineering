#import packages
from urllib.request import urlopen, Request


#specifying the url
url = 'https://masvida.org/'

#Package the request
request = Request(url)


# Send the request and catches the responses
response = urlopen(request)

#Extract the responses 
html = response.read()

#Printing the html content
print(html)

#close the conection
response.close()