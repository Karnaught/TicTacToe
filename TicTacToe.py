# -*- coding:UTF-8 -*-
def titulo():
    print("+ ================================================ +")
    print("+ -------------MASTERS OF TIC TAC TOE------------- +")
    print("+ ================================================ +")
    return

def tabuleiro():
    print("\n    ||   ||    ")
    print("  {a} || {b} || {c}  ".format(a = tab[1], b = tab[2], c = tab[3]))
    print("====||===||====")
    print("  {d} || {e} || {f}  ".format(d = tab[4], e = tab[5], f = tab[6]))
    print("====||===||====")
    print("  {g} || {h} || {i}  ".format(g = tab[7], h = tab[8], i = tab[9]))
    print("    ||   ||    ")
    return

def linha(tab):
    x1 = set(tab[0:3])
    x2 = set(tab[3:6])
    x3 = set(tab[6:])
    o = set(["O","O","O"])
    x = set(["X","X","X"])
    if x2 == o or x1 == o or x3 == o:
        print("{nome} fez uma linha".format(nome = p1))
        a = 1
        return a
    if x2 == x or x1 == x or x3 == x:
        print("{nome} fez uma linha".format(nome = p2))
        a = 1
        return a
    return

def coluna(tab):
    x1 = set([tab[0], tab[3], tab[6]])
    x2 = set([tab[1], tab[4], tab[7]])
    x3 = set([tab[2], tab[5], tab[8]])
    o = set(["O","O","O"])
    x = set(["X","X","X"])
    if x2 == o or x1 == o or x3 == o:
        print("{nome} fez uma coluna".format(nome = p1))
        a = 1
        return a
    if x2 == x or x1 == x or x3 == x:
        print("{nome} fez uma coluna".format(nome = p2))
        a = 1
        return a
    return

def diagonal(tab):
    x1 = set([tab[0], tab[4], tab[8]])
    x2 = set([tab[2], tab[4], tab[6]])
    o = set(["O","O","O"])
    x = set(["X","X","X"])
    if x2 == o or x1 == o:
        print("{nome} fez uma diagonal".format(nome = p1))
        a = 1
        return a
    if x2 == x or x1 == x:
        print("{nome} fez uma diagonal".format(nome = p2))
        a = 1
        return a
    return
repeat = 's'
while repeat != 'n':
    titulo()

    tab = [0,1,2,3,4,5,6,7,8,9]
    fim = 0
    rodada = 0
    result = False

    print("\nInsira o nome dos jogadores...\n")
    p1 = str(input("Jogador 1: "))
    p2 = str(input("Jogador 2: "))

    print("\n{nome} será O".format(nome = p1))
    print("{nome} será X".format(nome = p2))

    tabuleiro()
    tab = [" "," "," "," "," "," "," "," "," "," "]

    while rodada <= 8:

        if (rodada % 2) == 1:
            a = int(input("\n{nome} selecione um campo: ".format(nome = p2)))
            if tab[a] == " ":
                tab[a] = "X"
                print("\n")
                tabuleiro()
                rodada += 1
            elif tab[a] != " ":
                print("\nCampo utilizado, selecione outro.\n")
        fim_1 = linha(tab[1:])
        fim_2 = coluna(tab[1:])
        fim_3 = diagonal(tab[1:])
        if fim_1 == 1 or fim_2 == 1 or fim_3 == 1:
            result = True
            break

        if (rodada % 2) == 0:
            a = int(input("\n{nome} selecione um campo: ".format(nome = p1)))
            if tab[a] == " ":
                rodada += 1
                tab[a] = "O"
                print("\n")
                tabuleiro()

            elif tab[a] != " ":
                print("\nCampo utilizado, selecione outro.\n")
        fim1 = linha(tab[1:])
        fim2 = coluna(tab[1:])
        fim3 = diagonal(tab[1:])
        if fim1 == 1 or fim2 == 1 or fim3 == 1:
            break
    if rodada == 9 and result == False:
        print("\nJogadores empataram")
    print("\nFim de jogo")
    repeat = str(input("\nDeseja jogar novamente? ('s' ou 'n') "))
