# prime_numbers.py
# Script para mostrar los números primos entre 1 y 250
# y guardarlos en un archivo llamado results.txt

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


primos = []

# Buscar números primos entre 1 y 250
for n in range(1, 251):
    if es_primo(n):
        primos.append(n)

# Mostrar en pantalla
print("Números primos entre 1 y 250:")
for p in primos:
    print(p)

# Guardar resultados en archivo
with open("results.txt", "w") as archivo:
    for p in primos:
        archivo.write(str(p) + "\n")

print("\nResultados guardados en results.txt")