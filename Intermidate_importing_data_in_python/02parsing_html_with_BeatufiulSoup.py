#Import packages
import requests
from bs4 import BeautifulSoup

#specify the url
url = 'https://masvida.org/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

#Creating a beautifulsoup object
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)

