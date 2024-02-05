import random
import string

def criar_senha(tamanho):
    digitos = string.ascii_letters + string.digits
    texto_aleatorio = "".join(random.choice(digitos) for _ in range (int(tamanho)))
    return texto_aleatorio

tamanho_senha = int(input("Digite quantos caracteres tera a senha: "))
senha = criar_senha(tamanho_senha)

print(senha)