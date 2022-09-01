import random 

MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SIMBS = ['*', '+', '-', '/', '@', '_', '?', '!', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#']

def generate(passLength):
    CHARS = MAYUS + MINUS + NUMS + SIMBS
    passw = []

    for i in range(passLength + 1):
        randomChar = random.choice(CHARS)
        passw.append(randomChar)

    return ''.join(passw)

def run():
    while (True):
        passLength = int(input("Ingrese el numero de caracteres: "))
        passw = generate(passLength)
        print("Su contraseña es: " + passw)

if __name__ == '__main__':
    run()