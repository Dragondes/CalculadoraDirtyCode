def menu():
    print("""Menu
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Salir""")
def suma(numero1,numero2):
    reslutado = numero1 + numero2
    return reslutado

def resta(numero1,numero2):
    reslutado = numero1 - numero2
    return reslutado

def multiplicacion(numero1,numero2):
    reslutado = numero1 * numero2
    return reslutado
def division(numero1,numero2):
    reslutado = numero1 / numero2
    return reslutado

def calculadora():
    menu() #imprime menu
    opcion=int(input("Selecione Opcion\n"))
    
    while (opcion >0 and opcion <5):
        numero1 = int(input("Ingrese Numero\n"))    #primer numero para la operacion
        numero2 = int(input("Ingrese Otro Numero\n")) #segundo numero para la operacion
        
        if (opcion==1):      #elige la opcion para la operacion
            print("La Suma es:", suma(numero1,numero2))
            
        elif(opcion==2):
            print("La Resta es:",resta(numero1,numero2))
            
        elif(opcion==3):
            print("La Multiplicacion es:",multiplicacion(numero1,numero2))
            
        elif(opcion==4):
            print("La Division es:", division(numero1,numero2))            

        menu()
        opcion=int(input("Selecione Opcion\n"))       

calculadora()
