notas = []
for n in range(4):
    notas.append(float(input(f"Insira a {n+1}° nota: ")))

print(f"\rA media entre:\n{("\n").join(map(str,notas))}\né: {sum(notas)/len(notas)}")
