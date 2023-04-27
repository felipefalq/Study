# 1. Programa  em python para ler o valor do raio de um círculo, e depois mostrar o valor da área deste círculo com quatro casas decimais.

raio = float(input("Digite o valor do raio do círculo: "))

area = 3.14159 * raio**2

area_formatada = format(area, ".4f")

print("A área do círculo é:", area_formatada) 
