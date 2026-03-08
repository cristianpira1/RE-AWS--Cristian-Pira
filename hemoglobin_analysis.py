# En este archivo se ejecutara la tarea de el analisi de emoglobinas humanas#
# ---------------------------------------------------------
# hemoglobin_analysis.py
#
# Este script analiza una secuencia de proteína (hemoglobina)
# y calcula diferentes propiedades bioinformáticas como:
# - Longitud de la secuencia
# - Composición de aminoácidos
# - Peso molecular
# - Porcentaje de aminoácidos hidrofóbicos
#
# También guarda los resultados en un archivo JSON.
# ---------------------------------------------------------

import json

# Nombre de la proteína
protein_name = "Hemoglobin"

# Secuencia de ejemplo de hemoglobina
sequence = "VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHF"



# EJERCICIO 4: Mostrar información de la secuencia


print("Nombre de la proteína:", protein_name)
print("Secuencia:", sequence)
print("Longitud de la secuencia:", len(sequence))



# EJERCICIO 5: Calcular composición de aminoácidos


# Lista de aminoácidos
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

# Diccionario para guardar conteo
amino_count = {}

for aa in amino_acids:
    amino_count[aa] = sequence.count(aa)

print("\nConteo de aminoácidos:")
print(amino_count)



# EJERCICIO 6: Diccionario de pesos moleculares


amino_weights = {
"A": 89.09, "C": 121.15, "D": 133.10, "E": 147.13,
"F": 165.19, "G": 75.07, "H": 155.16, "I": 131.17,
"K": 146.19, "L": 131.17, "M": 149.21, "N": 132.12,
"P": 115.13, "Q": 146.15, "R": 174.20, "S": 105.09,
"T": 119.12, "V": 117.15, "W": 204.23, "Y": 181.19
}



# EJERCICIO 7: Función para calcular peso molecular


def calculate_molecular_weight(sequence):

    total_weight = 0

    for aa in sequence:
        if aa in amino_weights:
            total_weight += amino_weights[aa]

    return total_weight


molecular_weight = calculate_molecular_weight(sequence)

print("\nPeso molecular aproximado:", molecular_weight)



# EJERCICIO 9: Porcentaje de aminoácidos hidrofóbicos


hydrophobic = ["A","V","I","L","M","F","W","Y"]

hydrophobic_count = 0

for aa in sequence:
    if aa in hydrophobic:
        hydrophobic_count += 1

hydrophobic_percentage = (hydrophobic_count / len(sequence)) * 100

print("\nPorcentaje hidrofóbico:", hydrophobic_percentage, "%")



# EJERCICIO 8: Guardar resultados en JSON


results = {

"protein_name": protein_name,
"sequence_length": len(sequence),
"amino_acid_count": amino_count,
"molecular_weight": molecular_weight,
"hydrophobic_percentage": hydrophobic_percentage

}

with open("hemoglobin_results.json", "w") as file:
    json.dump(results, file, indent=4)

print("\nResultados guardados en hemoglobin_results.json")

