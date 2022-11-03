import random
def main():
    ruleta = []
    num_random = random.randint(1, 6)
    while True:
        try:
            numInp = int(input("Ingresa un número"))
        except ValueError:
            print("Debes ingresar un número")
            continue
        if numInp < 1 or numInp > 6:
            print("Debes ingresar un número del 1 al 6")
            continue
        if ruleta.count(numInp) == 0 and numInp != num_random: 
            print("Te salvas!")
            ruleta.append(numInp)
        elif ruleta.count(numInp) > 0:
            print("Ese número ya existe. Prueba con otro")
            continue 
        elif numInp == num_random:
            print("Bum!! Has perdido!")
            break
        if len(ruleta) == 5 and numInp != num_random:
            print(f"La bala es el número {num_random}")
            break
    while True:
        decisión = input("Escribe 'si' para volver a jugar o 'no' para terminar el juego")
        if decisión == "si":
            return main()
        elif decisión == "no":
            print("Hasta luego!")
            quit()
        else:
            print("El valor ingresado no es válido")
            continue

main()