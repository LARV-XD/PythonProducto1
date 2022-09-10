print("***MENU***")
print("1. agregar producto")
print("2. Mostrar Frutas")
print("3. SALIR")
opcion=100



frutas=[]

while(opcion!=3):
    Frutas={}
    opcion =int(input("Digite una opcion: "))
    if(opcion==1):
        frutas['sabor']=input("digite Nombre de la fruta: ")
        frutas['ingredientes']=[]
        for i in range(3):
            
            frutas['ingredientes'].append(input("Digita el nombre de la fruta: "))
        
        frutas['precioFabricacion']=input("digite precio de fabricacion: ")
        frutas['precioVenta']=input("digite precio de venta: ")
        frutas.append(frutas)
        print("agragando frutas")
    elif(opcion==2):
        
        print(frutas)
        print("Mostrando frutas")
    else:
        print("digite una opcion valida")
else:
    print("fin")

