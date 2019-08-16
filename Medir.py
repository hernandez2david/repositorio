import os

def bytesto(bytes, to, bsize=1024):
    """convert bytes to megabytes, etc.
       sample code:
           print('mb= ' + str(bytesto(314575262000000, 'm')))
       sample output: 
           mb= 300002347.946
    """

    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    for i in range(a[to]):
        r = r / bsize

    return(r)


# Programa que mide el tamanio de archivos en C:\Users\Public\Music\Sample Music y presenta el total en mb
os.chdir('C:\\Users\\Public\\Music\\Sample Music')  #para cambiar el directorio de trabajo
lista = []
lista = os.listdir('C:\\Users\\Public\\Music\\Sample Music')
file_size_bytes = 0

for element in range(len(lista)):
    file_size_bytes = int(os.path.getsize(str(lista[element])))

print("El tamano de archivos en la carpeta C:\\Users\\Public\\Music\\Sample Music es de " + str('%.3f'%bytesto(file_size_bytes, 'm')) + " Mb")
