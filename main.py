import secrets
import string

TAM_MIN = 4
TAM_MAX = 32
SIMBOLOS_PADRAO = "!@#$%^&*()-_=+[]{};:,.<>?/"

#so simbolos validos
def limpar_simbolos(texto):
    validos = ""
    for c in texto:
        if c.isalnum() or c.isspace() or c in validos:
            continue
        validos += c
    return validos

#gera a senha aleatória
def gerar_senha(tamanho, minusculas = True, maiusculas = True, numeros = True, simbolos = ""):
    if not TAM_MIN <= tamanho <= TAM_MAX:
        raise ValueError(f"O tamanho deve estar entre {TAM_MIN} e {TAM_MAX}.")

    grupos = []
    if minusculas:
        grupos.append(string.ascii_lowercase)
    if maiusculas:
        grupos.append(string.ascii_uppercase)
    if numeros:
        grupos.append(string.digits)
    if simbolos:
        validos = limpar_simbolos(simbolos)
        if not validos:
            raise ValueError("Nenhum símbolo válido")
        grupos.append(validos)

    if not grupos:
        raise ValueError("Escolha pelo menos um tipo de caractere.")

    senha = [secrets.choice(grupo) for grupo in grupos]

    alfabeto = "".join(grupos)
    senha += [secrets.choice(alfabeto) for _ in range(tamanho - len(senha))]

    secrets.SystemRandom().shuffle(senha)
    return "".join(senha)

#pergunta sim ou não pra cada caractere
def perguntar(texto):
    return input(f"{texto} [s/n]: ").strip().lower() != "n"

if __name__ == "__main__":
    texto = input ("Tamanho da sua senha:")
    if not  texto.isdigit():
        print ("Digite um número inteiro.")
    else:
        minusculas = perguntar("Inclui minúsculas (a-z)?")
        maiusculas = perguntar("Inclui maiúsculas (a-z)?")
        numeros = perguntar("Inclui números (0-9)?")
        simbolos = ""
        if perguntar("Inclui símbolos?"):
            simbolos = input(f"Símbolos aceitos (Enter = {SIMBOLOS_PADRAO}): ").strip()
            simbolos = simbolos or SIMBOLOS_PADRAO
        try:
            print (gerar_senha(int(texto), minusculas, maiusculas, numeros, simbolos))
        except ValueError as erro:
            print (erro)