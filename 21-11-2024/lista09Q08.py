meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

for mes in meses:
    temperaturas.append(float(input(f"Insira a temperatura do mês {mes}: ")))

media = sum(temperaturas)/len(temperaturas)
ordem = 1

print()
print("A média anual foi de:", format(media, ".2f"),"°C")
print("Os meses que estão acima da média são:")
print()

for index in range(len(meses)):
    if temperaturas[index] > media:
        print(f"{ordem} - {meses[index]}: {temperaturas[index]}°C")
        ordem += 1

