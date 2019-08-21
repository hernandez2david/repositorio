#funciones para abrir a traves del buscador
##nota, este solo jala en el IDLE
#import webbrowser
#webbrowser.open("http://inventwithpython.com/")

#requests lee el texto contenido en un sitio web (debe ser texto plano) y lo guarda en un archivo de texto
import requests
#recibe por parametro el sitio web
res = requests.get('https://www.w3.org/TR/PNG/iso_8859-1.txt')

res.raise_for_status()
playFile = open('w3School.txt', 'wb')
h
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
