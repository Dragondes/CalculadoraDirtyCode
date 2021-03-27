def Calculadora():
    print("""Menu
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Salir""")
    var = int(input("Selecione Opcion\n"))
    while (var >0 and var <5):
        x = int(input("Ingrese Numero\n"))
        y = int(input("Ingrese Otro Numero\n"))
        if (var==1):
            print("La Suma es:", x+y)
            var = int(input("Selecione Opcion\n"))
        elif(var==2):
            print("La Resta es:",x-y)
            var = int(input("Selecione Opcion\n"))
        elif(var==3):
            print("La Multiplicacion es:",x*y)
            var = int(input("Selecione Opcion\n"))
        elif(var==4):
            print("La Division es:", x/y)
            var = int(input("Selecione Opcion\n"))

#este codigo esta siendo refactorizado

Calculadora()
