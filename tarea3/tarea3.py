# ===========================
# FUNCIONES
# ===========================

# Consigna 2
def buscar_palabra(palabra, *lista):
    print("Palabra encontrada" if palabra in lista else "Palabra no encontrada")


# Consigna 3
def paridad(numero):
    print("Es par" if numero % 2 == 0 else "Es impar")


# Consigna 4
def promedio(*lista_nro):
    print(
        sum(lista_nro) / len(lista_nro)
        if lista_nro
        else "ERROR No ingreso valores en la lista ❌ El promedio es 0 "
    )


# Consigna 5


def mensaje_error(numero1, numero2, *numeros):
    print(f"{numero1 + numero2 + sum(numeros)}") if numeros else print(
        "ERROR Argumentos insuficientes. Debe agregar más numeros"
    )


# ==========================
# Llamadas
# ==========================

print("CONSIGNA 1: Mayor entre dos")

nro1 = int(input("Ingrese primer número 👉🏻"))
nro2 = int(input("Ingrese segundo número 👉🏻"))
mayor = nro1 if nro1 > nro2 else nro2

print(f"El mayor de los dos números es: {mayor}")


print("CONSIGNA 2: Palabra pérdida")

lista_ingresada = input("Ingrese palabras separadas por comas ✏️ ").split(",")
palabra_buscada = input("Ingrese la palabra que busca 🔎 ")

buscar_palabra(palabra_buscada, *lista_ingresada)

print("CONSIGNA 3: Analisis de Paridad")

numero_x = int(input("Ingrese el numero a analizar 👉🏻"))
paridad(numero_x)

print("CONSIGNA 4: Promedio preciso")

entrada = input("Ingrese la lista de numeros a promediar separados por coma 󰃬: ").split(
    ","
)
lista_promediar = list(map(int, entrada)) if entrada != [""] else []
promedio(*lista_promediar)

print("CONSIGNA 5: Mensaje de ERROR")
print("Ahora veremos que pasa si no proporciona los suficientes argumentos: ")
print("Se le pedira que ingrese unos numeros, no ingrese la lista de numeros")

arg1 = int(input("Ingrese primer argumento 👉🏻"))
arg2 = int(input("Ingrese segundo argumento 👉🏻"))
no_entrada = input("No ingrese estos numeros. Presione enter para continuar...")
arg3 = list(map(int, no_entrada)) if no_entrada != [""] else []
mensaje_error(arg1, arg2, *arg3)
