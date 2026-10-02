
try:
    a =int(input ('Ingrese el dividendo:: '))
    b =int(input ('Ingrese el divisor:: '))
   
    resultado = a/b
    print(f"El resultado de la división::{resultado}")
except ZeroDivisionError:
    print("El valor del divisor fue cargado con 0, valor inválido para la división")
except ValueError:
    print("Los valores no son válidos para esta operación")
    print("Valores aceptados: Numericos")


print(" ")
print("===========Pasemos a una suma==========")
a = "Cadena"
b = 10
try:
    a+b
except TypeError:
    print("Se intento sumar una cadena con un valor entero, la suma no admite esta operación")
    print("Transforme el entero a una cadena")

print(" ")
print("===========Pasemos a un diccionario============")
diccionario = {"error": "KeyError", "causa": "No existe una clave en el diccionario"}

try:
    print(diccionario["valor_valido"])
except KeyError:
    print("No existe la clave solicitada en el diccionario")
    print(f"Las llaves en el diccionario son: {diccionario}")

print(" ")
print("==================Pasemos a un archivo===========")

print("Intentaremos abrir el archivo test.txt. Por favor espere...")

try:
    with open("test.txt", "r") as test:
        print(test.read())
except FileNotFoundError:
    print("No existe dicho archivo. No se preocupe, lo resolveremos ;D")
    with open("test.txt", "w") as test:
        test.write("Test Operativo 001: Si puede leer esto no verá más excepciones")
    print("Se ha creado el archivo Test correctamente :D ! ")


