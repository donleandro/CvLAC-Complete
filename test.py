c#cvlac profe roman5690
#my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000105260'
#mi cvlac
my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000218430'
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
all = 0
a = 0
x = 0
y = 0
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("table")
for a in range(0,len(containers)):
    buscaEstrategias = containers[a].h3
    #print(buscaEstrategias)
    try:
        if buscaEstrategias.text == "Eventos científicos":
            all = a
            #print(all)
            break
    except AttributeError:
        pass

containerb = containers[all]
container = containerb.findAll("table")
cont = container[19]
info_evento = cont.td.text

b_eventos = cont.findAll("td")
productos = b_eventos[1].findAll("li")
prod = productos[y].text
index1 = prod.find("Nombre del producto:") + 20
index2 = prod.find("Tipo de producto:")
NombreProducto = prod[index1:index2]

print(NombreProducto.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))
