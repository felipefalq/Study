# 2. Programa para ler o código de um produto, a quantidade de produtos e o valor unitário de cada produto (1) +
#o código de um produto, a quantidade de produtos e o valor unitário de cada produto (2). 

# Produto 1 #
idProd1 = input("Digite o código do primeiro produto: ")
quantidadeProd1 = int(input("Digite a quantidade de produtos: "))
valorProd1 = float(input("Digite o valor unitário de cada produto: "))
print ("\n")

# Produto 2 #
idProd2 = input("Digite o código do segundo produto: ")
quantidadeProd2 = int(input("Digite a quantidade de produtos: "))
valorProd2 = float(input("Digite o valor unitário de cada produto: "))

valorProd1 = quantidadeProd1 * valorProd1
valorProd2 = quantidadeProd2 * valorProd2
valor_total_pago = valorProd1 + valorProd2

print("Valor total a ser pago: R$", valor_total_pago)