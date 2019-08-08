import random

   
def evaluar(dado,guessfun): 
    clue = ""
    try:
        if guessfun < dado:
            clue = 'El numero dado es mayor'
        elif guessfun > dado:
            clue = 'El numero dado es menor'
        print(clue)
    except Exception:
        print("Hey comps, solo usamos numeros aqui ")


name = str(input('Humano, comencemos, puedes indicarme tu nombre: '))
intentos = 0
guess = random.randint(1,20)
dado = 0

while guess != dado:
    dado = input('Dame un numero entre 1 y 20 ')
    evaluar(dado,guess)
    intentos += 1

print('Felicidades ' + name + ' El numero ' + str(dado) + ' Es correcto, Solo te tomo ' + str(intentos) + ' intentos')
