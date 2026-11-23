#Calculadora de Desconto 
#(Fundamentos): Peça o preço de um produto e a porcentagem de desconto.
#Calcule e exiba o valor economizado e o preço final formatados com duas casas 
#decimais.
preco = float(input("Digite o preço do produto (R$):"))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%)"))
valor_economizado = preco * (porcentagem_desconto / 100)
preco_final = preco - valor_economizado

print (f"Valor economizado: R$ {valor_economizado: .2f}")
print (f"Preço final com desconto: R$ {preco_final: .2f}")

