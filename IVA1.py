#Programa estandard

#Precio original
print ("Escribe el precio con solo 2 decimales:")
Precio = float(input())
#Se añade "float" para permitir decimales

#IVA
print ("¿Que IVA quieres añadir?")
x= 4
y= 10
z= 21
print ("4%, 10% o 21%?")

IVA = int(input())

#Valores verdaderos:
IVA1 = 104/100
IVA2 = 110/100
IVA3 = 121/100

#Resultados
if IVA == x:
    print ("El precio total es:" , Precio * IVA1)

if IVA == y:
    print ("El precio total es:" , Precio * IVA2)

if IVA == z:
    print ("El precio total es:" , Precio * IVA3)

#Echo en python por Jaureo
