### Ejercicios CICLOS

def triangulo1():
    while (True):
        cont = 0
        num = int(input("Ingrese un número: "))
        ch = ""
        while(cont < num):
            ch += "*"
            print(ch)
            cont += 1

def triangulo2():
    while True:
        cont = 0
        num = int(input("Ingrese un número: "))
        numAux = 1
        cadena = ""
        while(cont < num):
            cadena += str(numAux)
            print(cadena[::-1])
            numAux += 2
            cont += 1

def contraseña():
    usuario = ""
    passw = ""
    u = ""
    p = ""

    result = False
    while(not result):
        opc = input("""
            Seleccione una opción:

            1.- Iniciar sesion
            2.- Registarse
        """)

        if(opc == "2"):
            usuario = input("Ingrese el usuario: ")
            passw = input("Ingrese la contraseña: ")
            print("Registrado correctamente...")     
        else:
            if(usuario == ""):
                print("Aún no se ha registrado")
            else:
                u = input("Ingrese el usuario: ")
                p = input("Ingrese la contraseña: ")
                if(usuario == u and passw == p):
                    print("Ha ingresado correctamente")
                    result = True
                else:
                    print("Contraseña o Usuario incorrecto")



contraseña()