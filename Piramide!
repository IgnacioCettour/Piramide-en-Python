def piramide(cantidad_palitos:int)-> int:
    
    fila:int = 1
    palitos_impresos:int = 1

    espacio:str = " "
    espacios_fila:int = 50 #Esta variable es la que multiplica a los espacios para que la piramide no quede pegada a la izquierda

    while palitos_impresos <= cantidad_palitos:


        print((espacio*espacios_fila)+("| " * fila)) #El espacio despues del | es para que sea simetrico respecto a las otra filas

        espacios_fila -= 1
        
        fila += 1
        palitos_impresos += fila

    return cantidad_palitos

piramide(21) #ejemplo de 21 |, vos despues declaras en main con tus variables!!
