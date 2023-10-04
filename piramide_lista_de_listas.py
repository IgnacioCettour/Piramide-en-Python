piramide:list = []
filas:int = 4
n:int = 1

for elemnto in range(filas):

    espacios:str = " " * filas
    palitos:str = "| " * n

    piramide.append(espacios+palitos)

    filas -= 1
    n += 1

for elemento in piramide:

    print(elemento)
