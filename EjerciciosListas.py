### Ejercicios CICLOS
def horario():
    lista = []
    band = True
    while band:
        materia = input("Materia: ")
        if (materia == "."):
            band = False
        else:
            lista.append(materia)

    print(lista)



def capitalizar():
    while True:
        cadena = input("Cadena: ")
        arrCadena = cadena.split(" ")

        text = ""
        for x in arrCadena:
            text += x.capitalize() + " "
        print(text)

capitalizar()
#horario()