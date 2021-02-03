def es_palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    return palabra[::] == palabra[::-1]


def run():
    while True:
        palabra = input('Ingrese una palabra: ')
        if es_palindromo(palabra):
            print('Es palindromo')

        else:
            print('No es palindromo')
            break


if __name__ == "__main__":
    run()
    print('Gracias por utilizar nuestro palindodromo')