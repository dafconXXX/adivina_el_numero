import random

def run():
    numero_aleotorio = random.randint(1, 10)
    numero_elegido = int(input("Ingrese un numero: "))
    while numero_elegido != numero_aleotorio:
        if numero_aleotorio > numero_elegido:
            print('El numero buscado es mayor')
        else:
            print('El numero buscado es una menor cantidad')
        numero_elegido = int(input("Ingrese otro numero: "))
    print("Ganaste!!!")



if __name__ == "__main__":
    run()