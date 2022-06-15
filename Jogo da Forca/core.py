import os
import sys


# Função limpar console
def cleanWindows():
    os.system("cls")


# Opções para o jogador
def menuChoices():
    print("(1) Jogar (2) Solicitar Dica")
    x = input()
    return x


# Inserir uma letra
def play():

    while True:
        try:
            letter = input("Digite uma letra: ")
            finalLetter = letter.upper()
            if len(finalLetter) > 1 or len(finalLetter) == 0:
                print("Você precisa inserir uma letra!")
                pass
            else:
                return finalLetter
            break
        except:
            pass


# Desafiante define a palavra
def chooseWord():
    while True:
        word = input("Escolha a palavra chave: ")
        finalWord = word.upper()
        if len(finalWord) == 0:
            print("Insira uma palavra!")
        else:
            keyWord = []
            for letter in finalWord:
                try:
                    teste = int(letter)
                except:
                    letter.upper()
                    keyWord.append(letter)
            return keyWord


def game(x, y, z):
    e = 0
    aux = 0
    for i in range(0, len(y)):
        if x == y[i]:
            z[i] = x
            aux = 1
    if aux == 0:
        return e + 1
    else:
        return 0


# A view do jogo
def wordView(x, y, e):
    print(f"Erros: {e}")
    print("A palavra escolhida é:")
    print(x)
    print(f"A palavra possui {len(y)} letras.")


# Cria o arquivo de historico de partida
def logAdd(v, x, y, z):
    if v == 1:
        archive = open("history.txt", "r")
        dataHistory = archive.readlines()
        dataHistory.append("Palavra: ")
        dataHistory.append(x)
        dataHistory.append(" Vencedor: ")
        dataHistory.append(y)
        dataHistory.append(" Perdedor: ")
        dataHistory.append(z)
        dataHistory.append("\n")
        archive = open("history.txt", "w")
        archive.writelines(dataHistory)

        archive = open("history.txt", "r")
        text = archive.readlines()
        for line in text:
            print(line)
        archive.close()


# Opção de reiniciar ou sair do jogo
def restartMenu():
    while True:
        try:
            x = 0
            x = int(input("[1] Reiniciar [2] Sair "))
            if x == 1 or x == 2:
                return x
                break
            else:
                print("Insira uma opção válida!")
                print("")
        except:
            print("Insira uma opção válida!")
            print("")
