import random

def escolher_palavra():
    palavras = ["python", "java", "ruby", "javascript", "html", "css", "tenis", "monitor", "jogos", "escola", "caderno", "jornal", "teclado",
                "fones", "felipe neto", "react", "processador", "engenheiro", "advogado", "ceu", "controle"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao.strip()

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6  # Número máximo de tentativas permitidas

    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0:
        print("\nPalavra: {}".format(exibir_palavra(palavra_secreta, letras_corretas)))
        letra_escolhida = input("Escolha uma letra: ").lower()

        if letra_escolhida in letras_corretas:
            print("Você já escolheu essa letra. Tente novamente.")
            continue

        if letra_escolhida in palavra_secreta:
            letras_corretas.append(letra_escolhida)
            print("Letra correta!")
        else:
            tentativas -= 1
            print("Letra incorreta. Tentativas restantes: {}".format(tentativas))

        if set(letras_corretas) == set(palavra_secreta):
            print("\nParabéns! Você acertou a palavra: {}".format(palavra_secreta))
            break

    if tentativas == 0:
        print("\nGame over! A palavra correta era: {}".format(palavra_secreta))

if __name__ == "__main__":
    jogar_forca()
