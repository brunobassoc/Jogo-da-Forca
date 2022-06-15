import os
import sys
from core import cleanWindows, menuChoices, play, chooseWord, game, wordView, logAdd, restartMenu

init = 1

while init == 1:
    challenger = input("Insira o nome do Desafiante: ")
    player = input("Insira o nome do jogador: ")

    player_winner = 0
    challenger_winner = 0

    cleanWindows()

    uncovered = []

    word = chooseWord()

    hint1 = input("1º Dica: ")
    hint2 = input("2º Dica: ")
    hint3 = input("3º Dica: ")
    hintRequests = 0
    counter = 0
    limit = 0
    cleanWindows()

    hit = False

    for l in range(0, len(word)):
        uncovered.append("_")
    while hit == False:
        print(f"Erros: {counter}")
        print("A palavra escolhida é:")
        print(uncovered)
        print(f"Ela possui {len(word)} letras.")
        print("")
        option = menuChoices()
        if option == "2":
            hintRequests += 1
            if hintRequests == 1:
                cleanWindows()
                print(f"1º Dica: {hint1}")
                print("")
                wordView(uncovered, word, counter)
                print("")
                attempt = play()
                counter += game(attempt, word, uncovered)
                cleanWindows()
                if counter == 5:
                    limit = 1
                    break
                if uncovered == word:
                    hit = True
                    break
            elif hintRequests == 2:
                cleanWindows()
                print(f"2º Dica: {hint2}")
                print("")
                wordView(uncovered, word, counter)
                print("")
                attempt = play()
                counter += game(attempt, word, uncovered)
                cleanWindows()
                if counter == 5:
                    limit = 1
                    break
                if uncovered == word:
                    hit = True
                    break
            elif hintRequests == 3:
                cleanWindows()
                print(f"3º Dica: {hint3}")
                print("")
                wordView(uncovered, word, counter)
                print("")
                attempt = play()
                counter += game(attempt, word, uncovered)
                cleanWindows()
                if counter == 5:
                    limit = 1
                    break
                if uncovered == word:
                    hit = True
                    break
            else:
                cleanWindows()
                print("Limite de dicas excedido!")
                print("")
                wordView(uncovered, word, counter)
                print("")
                attempt = play()
                counter += game(attempt, word, uncovered)
                cleanWindows()
                if counter == 5:
                    limit = 1
                    break
                if uncovered == word:
                    hit = True
                    break
        elif option == "1":
            cleanWindows()
            wordView(uncovered, word, counter)
            print("")
            attempt = play()
            counter += game(attempt, word, uncovered)
            cleanWindows()
            if counter == 5:
                limit = 1
                break
            if uncovered == word:
                hit = True
                break

            if uncovered == word:
                hit = True
                break

    if hit == True:
        cleanWindows()
        print(f"{player}você venceu!")
        player_winner = 1
        word = str(word)
        logAdd(player_winner, word, player, challenger)
        finalOption = restartMenu()
        if finalOption == 1:
            cleanWindows()
            pass
        else:
            init = 0
            cleanWindows()

    if limit == 1:
        cleanWindows()
        print(f"{challenger} você venceu!")
        challenger_winner = 1
        word = str(word)
        logAdd(challenger_winner, word, challenger, player)
        finalOption = restartMenu()
        if finalOption == 1:
            cleanWindows()
            pass
        else:
            init = 0
            cleanWindows()