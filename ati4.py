#Enunciado: Peça um número inteiro não negativo ao usuário. 
#Enquanto ele digitar um número negativo, peça novamente.
#Quando válido, calcule e exiba o fatorial desse número ($N!$)
numero = int(input("Digite um número inteiro não negativo: "))

while numero < 0:
    print("Número inválido! O valor não pode ser negativo.")
    numero = int(input("Digite um número inteiro não negativo: "))

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} ({numero}!) é {fatorial}.")