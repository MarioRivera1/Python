# Mario Rivera :D

# PROBLEMA 01 

# Elaborar un programa para una ferretería que genere 
# la boleta de venta, tener en cuenta lo siguiente:
# La ferretería tiene una política de descuento sobre 
# el valor de la compra de acuerdo al siguiente cuadro:
# Valor de compra: 0  - 50  --> 5%
# Valor de compra: 51 - 150 --> 8%

print("======================================")
print("=       Ferreteria Mario's           =")
print("======================================")
print()
print("BIENVENID@")
import datetime
fechaActual = datetime.datetime.now()
print("FECHA : ",fechaActual)
print()
print("Digite su pedido  ")
p = input("Ingrese nombre del producto : ")  #Producto
vp = float(input("Ingrese el valor del producto : "))  #Valor del producto
cant = int(input("Ingrese la cantidad : "))
vc = vp*cant  #Valor de la compra
if vc <= 50:
    desc = vc * 0.05
elif vc <= 150:
    desc = vc * 0.08
else:
    desc = 0
print()
fdesc = vc - desc   #Prefio final con descuento

print("Subtotal: ", vc)
print(f"Descuento: {desc}")
print(f"Total: {fdesc}")

print()
print("Gracias por su compra")
print()

#PROBLEMA 02

# Crear un programa que ingrese n numeros y determine
# el promedio de los mismos
print("======================================")
print("=          PROMEDIO                  =")
print("======================================")
print()
print("BIENVENID@")
print()

num = []
n = int(input("Cuantos numeros va a ingresar : "))
i = 0
while i < n:
    val = int(input(f"Ingrese el valor {i+1} : "))
    num.append(val)
    i+=1
prom = sum(num)/len(num)
print("El promedio es : ",prom)

# PROBLEMA 03

# Usando While elabora un programa que 
# genere los 100 elementos de la siguiente serie
## 1, 2, 4, 8, 16,	….

print("======================================")
print("=          Bucle 1 2 4 8 16 ...      =")
print("======================================")
print()
print("BIENVENID@")
print()
num = 1
i = 0 
while i < 100: 
    print(num) 
    num *= 2  #num = num * 2 
    i += 1

# PROBLEMA 04

#Crea un programa que ingrese un número de 3 cifras y determine si es capicúa.

print("======================================")
print("=          Numero Capicua            =")
print("======================================")
print()
print("BIENVENID@")
print()
n = int(input("Ingrese un numero de 3 digitos: "))
if n > 99 and n <1000:
    a = n//100  #Cociente
    b = n%10  #Residuo
    if a==b:
        print("EL numero",n, "es capiua")
    else:
        print("El numero",n,"No es capicua")
else:
    print("INCORRECTO")
    n = int(input("Ingrese un numero de 3 digitos : "))

print()

#PROBLEMA 05

# Crea un programa que almacene en listas los nombres, edad y nota de un salón de clase
print("======================================")
print("=          Lista                     =")
print("======================================")
print()
print("BIENVENID@")
print()
nombres = [] 
edades = [] 
notas = [] 

cuantos_estudiantes_son = int(input("Cuantos estudiantes son: ")) 

for i in range(cuantos_estudiantes_son): 
    nombre = input("Ingrese el nombre: ") 
    edad = int(input("Ingrese la edad : ")) 
    nota = float(input("Ingrese la nota : ")) 

    nombres.append(nombre) 
    edades.append(edad) 
    notas.append(nota) 

 

print("Los nombres de los estudiantes son : ", nombres) 
print("Las edades de los estudiantes son : ", edades) 
print("Las notas de los estudiantes son : " , notas)

#PROBLEMA 06

# Crea un programa que calcule cuantos baldes de agua (8 litros) 
# se necesita para llenar un pozo de n miles de litros de agua.
print("======================================")
print("=          Problema 06               =")
print("======================================")
print()
print("BIENVENID@")
print()

n = int(input("Cuantos miles de litros necesitas para llenar el pozo : "))
print()
balde = 8  #cada balde tiene capacidad de 8 litros. 

while n < 1000 or n > 10000:
    print("¡Incorrecto!, ingrese un numero de 4 digitos")
    n = int(input("Cuantos miles de litros necesitas para llenar el pozo : "))
    print()

tbaldes = n/balde  #Total de baldes
print("Vamos a necesitar ",tbaldes," baldes, para llenar el pozo de ",n," litros.")
