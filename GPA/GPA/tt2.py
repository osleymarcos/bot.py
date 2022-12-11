from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.metro.sp.gov.br/sua-viagem/trajeto/')
soup = BeautifulSoup(html, 'html.parser')
linha_1 = soup.findAll(class_='linha-1-azul')
#Itera por cada elemento e obtido na consulta...
for e in linha_1:
  print(e.get_text())


