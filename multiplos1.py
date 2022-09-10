print("Ejercicio 1")

NroCantidad=int(input("Digite el numero: "))
Cantidad = 0
Cantidad1= 0


while Cantidad <= NroCantidad:
    if(Cantidad % 3) == 0:
        print(Cantidad,end=",")
    Cantidad = Cantidad + 1
    print(f'Multiplos 3 : {Cantidad}')

while Cantidad1 <= NroCantidad:
    if(Cantidad1 % 2) == 0:
        print(Cantidad1,end=",")
    Cantidad1 = Cantidad1 + 1
    print(f'Multiplos  2 : {Cantidad1}')
