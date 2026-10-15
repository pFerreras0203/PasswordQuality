import secrets
import string

TAM_MIN = 4
TAM_MAX = 128

#gera a senha aleatória
def gerar_senha(tamanho):
    if not TAM_MIN <= tamanho <= TAM_MAX:
        raise ValueError(f"O tamanho deve estar entre {TAM_MIN} e {TAM_MAX}.")
    alfabeto = string.ascii_letters + string.digits
    return "".join(secrets.choice(alfabeto)for _ in range(tamanho))

if __name__ == "__main__":
    texto = input ("Tamanho da sua senha:")
    if not  texto.isdigit():
        print ("Digite um número inteiro.")
    else:
        try:
            print (gerar_senha(int(texto)))
        except ValueError as erro:
            print (erro)