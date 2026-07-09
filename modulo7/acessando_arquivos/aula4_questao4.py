import random
import os

estagios_enforcado = []

def carrega_arquivos():
    global estagios_enforcado

    diretorio_script = os.path.dirname(os.path.abspath(__file__))

    caminho_palavras = os.path.join(diretorio_script, "gabarito_forca.txt")
    caminho_desenhos = os.path.join(diretorio_script, "gabarito_enforcado.txt")

    with open(caminho_palavras, "r", encoding="utf-8") as f:
        palavras = [linha.strip().upper() for linha in f.readlines() if linha.strip()]

    with open(caminho_desenhos, "r", encoding="utf-8") as f:
        conteudo = f.read()
        estagios_enforcado = conteudo.split("\n\n")
        
    return palavras

def imprime_enforcado(erros):
    if erros < len(estagios_enforcado):
        print(estagios_enforcado[erros])

def jogar():
    palavras = carrega_arquivos()
    palavra_secreta = random.choice(palavras)

    palavra_oculta = ["_"] * len(palavra_secreta)
    erros = 0
    tentativas_maximas = 6
    letras_chutadas = []

    print("\nBem-vindo ao Jogo da Forca!")

    while erros < tentativas_maximas and "_" in palavra_oculta:
        print(f"\nPalavra: {' '.join(palavra_oculta)}")
        print(f"Letras já tentadas: {', '.join(letras_chutadas)}")
        
        chute = input("Digite uma letra: ").upper().strip()

        if len(chute) != 1 or not chute.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue
            
        if chute in letras_chutadas:
            print("Você já tentou essa letra!")
            continue

        letras_chutadas.append(chute)

        if chute in palavra_secreta:
            print("-> Acertou!")
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == chute:
                    palavra_oculta[i] = chute
        else:
            print("-> Errou!")
            erros += 1
            imprime_enforcado(erros)

    print("\n" + "="*20)
    if "_" not in palavra_oculta:
        print(f"Parabéns! Você venceu! A palavra era '{palavra_secreta}'.")
    else:
        print(f"Game Over! Você foi enforcado. A palavra era '{palavra_secreta}'.")

if __name__ == "__main__":
    jogar()