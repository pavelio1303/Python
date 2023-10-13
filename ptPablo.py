import random

def escalonesTotales(cuantosEscalones):
    escalonesCasa = random.randrange(50,cuantosEscalones+1)
    return escalonesCasa

"""
def escalonesNo(escalonesTotales):
    escalonesCasa = escalonesTotales
    for escalon in escalonesCasa:
        if escalon == escalon%13:
            print (f"no podemos pisar el escalón {escalon}")
"""
         
def giroTimbre():
    giros = 6
    for giro in range(5):   
        giros -= 1
        print(f"Tengo que girar {giros} veces.")

# Ejercicio 1 (Escalones)

numeroEscalonesMax = 150
escalonesFinales = escalonesTotales(numeroEscalonesMax)
#escalonesNoPisar = escalonesNo(escalonesFinales)

print(f"Tenemos {escalonesFinales} escalones que subir.")
#print(f"Evitando el escalón {escalonesNoPisar}.")

# Ejercicio 2 (Timbre)

vecesGirando = giroTimbre()

print(f"{vecesGirando}")

#print(giroTimbre)
