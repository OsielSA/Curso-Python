VALOR_DOLAR = 20.03

def convertir(opcion, cantidad):
    if opcion == "1":
        convertida = cantidad / VALOR_DOLAR
        moneda = "dolares"
    else:
        convertida = cantidad * VALOR_DOLAR
        moneda = "pesos"

    convertida = round(convertida, 2)
    convertida = str(convertida)
    print("Cantidad en " + moneda + ": $" + convertida)



menu = """
    Elije:

    1 - Dolar a peso
    2 - Peso a dolar
"""
opcion = input(menu)
cantidad = float(input("Ingrese la cantidad a convertir: "))

convertir(opcion, cantidad)

