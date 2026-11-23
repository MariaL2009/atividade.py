#Enunciado: Leia o ano de nascimento de uma pessoa, 
# calcule sua idade atual e informe se o voto é proibido (menor de 16 anos), 
# facultativo (16, 17 ou acima de 70 anos) ou obrigatório (entre 18 e 70 anos).

from datetime import date
ano_nascimento = int(input("Digite o ano de nascimento:"))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento 

print (f"Você tem {idade}anos.")

if idade < 16:
    print("Situaçaõ do voto: PROIBIDO.")
elif (16 <= idade < 18) or (idade >70):
    print ("Situação do voto: FACULTATIVO.")
else: 
    print ("Situação do voto: OBRIGATÓRIO.")
    
