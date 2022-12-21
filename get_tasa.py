import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

link = "https://www.bcv.org.ve/"
f = urllib.request.urlopen(link)
myfile = f.read()
soup = BeautifulSoup(myfile, 'html.parser')
div_dolar = str(soup.find(id="dolar").strong)

print(div_dolar.split()[1])
