from random import randint

limite_inferior = int(input("Ingrese el limite inferior: "))
limite_superior = int(input("Ingrese el limite superior: "))

if limite_inferior >= limite_superior:
    print("Error: el limite inferior debe ser menor que el limite superior")
else:
    print("Rango Correcto")

    numero = randint(limite_inferior, limite_superior)

    if numero % 2 != 0:
        if numero +1 <= limite_superior:
            numero_final = numero + 1
        else:
            numero_final = numero - 1
    else:
        numero_final = numero

    intentos = 1
    adivino = False

    intento1 = 0
    intento2 = 0

    while intentos <= 3 and adivino == False:
        intento = int(input(f"intento {intentos}: "))

        if intento == numero_final:
            print("Felicitaciones, pudiste adivinar")
            adivino = True
        else:
            if intento < numero_final:
                print("El numero es mayor")
            else:
                print("El numero es menor")

        if intentos == 1:
            intento1 = intento
        elif intentos == 2:
            intento2 = intento

            distancia1 = abs(numero_final - intento1)
            distancia2 = abs(numero_final - intento2)

            print("Te dare una pista:")

            if distancia1 < distancia2:
                print("El numero esta mas cerca de", intento1, "que de", intento2)
            elif distancia2 < distancia1:
                print("El numero esta mas cerca de", intento2, "que de", intento1)
            else:
                print("Ambos intentos estuvieron igual de cerca")

        intentos += 1

    if adivino == False:
        print("Perdiste")
        print("El numero era:", numero_final)