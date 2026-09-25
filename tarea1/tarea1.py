a = {1, 22, 3, 53, 99}
b = {3, 22, 33, 45, 90}


print("Consigna 1: En A o B o ambos: ", a | b)

print("Consigna 2: En A y B: ", a & b)
print("Consigna 3: En A o en B, no en ambos: ", a.symmetric_difference(b))
print("Consigna 4: ¿A es subconjunto de B?: ", a.issubset(b))
print("Consigna 5: Número de Elementos de A: ", len(a))
