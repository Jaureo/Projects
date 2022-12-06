#Este programa permite calcular con más decimales

#Precio original
print ("Escribe el precio sin centimos:")
Euros = int(input())
print ("Escribe los centimos")
Centimos = int(input())

#Convertimos en decimales los centimos
Decimales = Centimos/100

#Sumamos Eureos y centimos
Precio = Euros + Decimales

#IVA
print ("¿Que IVA quieres aplicar?")
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
