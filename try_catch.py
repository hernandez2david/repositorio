#Try and catch example python

#python 3.5.2
print("Cuantos gatos tienes? ")

numcats = input("Cuantos gatos tienes ")
try: 
    if int(numcats) >= 4:
        print(" Bastantes gatos ")
    else:
        print("No son suficientes gatos ")
except ValueError:
    print("No se ingreso ningun numero ")
