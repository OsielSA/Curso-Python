import random

def run():
    numeroAleatorio = random.randint(1, 101)
    print("(" + str(numeroAleatorio) + ")")
    numeroUsuario = int(input("Elige un número del 1 al 100: "))

    encontrado = False
    while not encontrado:
        if(numeroUsuario > numeroAleatorio):
            numeroUsuario = int(input("Elige un número menor: "))
        elif (numeroUsuario < numeroAleatorio):
            numeroUsuario = int(input("Elige un número mayor: "))
        else:
            print("CORRECTO!!")
            encontrado = True


if __name__ == '__main__':
    run()