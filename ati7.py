#Enunciado: Implemente uma Cifra de César simples: receba uma mensagem e 
#um número de deslocamento (chave) e retorne o texto criptografado deslocando 
#cada letra no alfabeto.
def cifra_de_cesar(texto: str, chave: int) -> str:
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Define a base ASCII ('A' = 65 para maiúsculas, 'a' = 97 para minúsculas)
            base = ord('A') if char.isupper() else ord('a')
            # Desloca a letra mantendo o ciclo de 26 letras do alfabeto
            novo_codigo = (ord(char) - base + chave) % 26 + base
            resultado += chr(novo_codigo)
        else:
            # Mantém espaços, números e pontuações inalterados
            resultado += char
            
    return resultado

mensagem = input("Digite a mensagem para criptografar: ")
deslocamento = int(input("Digite a chave (número de posições): "))

print("Mensagem criptografada:", cifra_de_cesar(mensagem, deslocamento))