n = int(input("Digite cantidad de numeros que desea ingresar: "))
contador = 0
contadorMultiplos2 = 0
contadorMultiplos3 = 0

while(contador < n):
    numero = int(input("Digite numero entero: "))
    contador+=1
    if(numero % 2 == 0 and numero % 3 == 0):
        contadorMultiplos2+=1
        contadorMultiplos3+=1
        print(f'{numero} es multiplo de 2 y 3')
    elif(numero % 2 == 0):
        contadorMultiplos2+=1
        print(f'{numero} es multiplo de 2')
    elif(numero % 3 == 0):
        contadorMultiplos3+=1
        print(f'{numero} es multiplo de 3')
    else:
        print(f'{numero} no es multiplo de 2 ni de 3')

print(f'Los multiplos de 2 son {contadorMultiplos2}')
print(f'Los multiplos de 3 son {contadorMultiplos2}')
