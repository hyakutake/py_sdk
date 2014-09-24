import copy

# Funcao principal onde o puzzle e resolvido
def Resolver(PUZZ):
    # Criar copia do puzzle original
    PUZZ_ORIGINAL = copy.deepcopy(PUZZ)

    # Imprimir o puzzle a resolver
    print("A resolver")
    ImprimirPuzzle(PUZZ)

    # Definir posicoes e valores iniciais
    posLin = 0
    posCol = 0
    hipotese = 1

    # Ciclo onde e resolvido o puzzle
    while 1:
        # Verificar se celula esta vazia na posicao posCol, posLin
        while VerificarCelulaVazia(PUZZ, posLin, posCol) == 0:
            posCol += 1
            if posCol > 8:
                posCol = 0;
                posLin += 1
                # Verificar se chegou ao fim do puzzle
                if posLin > 8:
                    print("Resolvido")
                    ImprimirPuzzle(PUZZ)
                    return 1


        # Verificar se e valido nas linhas, colunas e blocos; sendo a soluÃ§Ã£o menor que 10
        if VerificarHipoteseLinha(PUZZ, posLin, hipotese) == 1 and VerificarHipoteseColuna(PUZZ, posCol, hipotese) == 1 and DeterminarBloco(PUZZ, hipotese, posLin, posCol) == 1 and hipotese < 10:
            PUZZ[posLin][posCol] = hipotese
            #print("Atribuido a hipotese", hipotese, "em", posLin, posCol)
            hipotese = 1
        else:
            hipotese += 1
            # Retroceder
            if hipotese > 9:
                posLin, posCol = Retroceder(PUZZ_ORIGINAL, posLin, posCol)
                hipotese = PUZZ[posLin][posCol] + 1
                PUZZ[posLin][posCol] = 0
    pass

# Retroceder para a posicao anterior
def Retroceder(PUZZ_ORIGINAL, posLin, posCol):
    posCol -= 1
    if posCol < 0:
        posCol = 8
        posLin -= 1
        if posLin < 0:
            print("ALGUMA COISA CORREU MAL! POSSIVELMENTE PUZZLE SEM SOLUCAO")
            exit()

    while VerificarCelulaVazia(PUZZ_ORIGINAL, posLin, posCol) == 0:
        posCol -= 1
        if posCol < 0:
            posCol = 8
            posLin -= 1
        if posLin < 0:
            print("ALGUMA COISA CORREU MAL! POSSIVELMENTE PUZZLE SEM SOLUCAO")
            exit()
    return posLin, posCol
    pass

# Determinar bloco em que esta a posicao
# Devolve 1 se hipotese for possivel, 0 se for invalido
def DeterminarBloco(PUZZ, hipotese, posLin, posCol):
    # Para linhas
    if posLin >= 0 and posLin <= 2:
        BlocoLin = 0;
    if posLin >= 3 and posLin <= 5:
        BlocoLin = 1;
    if posLin >= 6 and posLin <= 8:
        BlocoLin = 2;
    # Para colunas
    if posCol >= 0 and posCol <= 2:
        BlocoCol = 0
    if posCol >= 3 and posCol <= 5:
        BlocoCol = 1
    if posCol >= 6 and posCol <= 8:
        BlocoCol = 2

    # Verificar bloco para a hipotese
    for a in range (0, 3):
        for b in range (0, 3):
            if PUZZ[a + 3 * BlocoLin][b + 3 * BlocoCol] == hipotese:
                #print ("Hipotese", hipotese, "invalido no bloco", BlocoLin, BlocoCol)
                return 0
    #print ("Hipotese", hipotese, "possivel no bloco", BlocoLin, BlocoCol)
    return 1
    pass

# Verificar se a hipotese existe na linha
# Devolve 1 se hipotese for possivel na linha, 0 se nao for possivel
def VerificarHipoteseColuna(PUZZ, posCol, hipotese):
    for a in range (0, 9):
        if PUZZ[a][posCol] == hipotese:
            #print("Hipotese", hipotese, "invalido na coluna", posCol)
            return 0
    #print ("Hipotese", hipotese, "possivel na coluna", posCol)
    return 1
    pass

# Verificar se a hipotese existe na linha
# Devolve 1 se hipotese for possivel
def VerificarHipoteseLinha(PUZZ, posLin, hipotese):
    for a in range (0, 9):
        if PUZZ[posLin][a] == hipotese:
            #print("Hipotese", hipotese, "invalido na linha", posLin)
            return 0
    #print ("Hipotese", hipotese, "possivel na linha", posLin)
    return 1
    pass

# Verificar se a linha no puzzle original esta vazia
# Devolve 1 se vazio 0 se cheio
def VerificarCelulaVazia(PUZZ, posLin, posCol):
    if PUZZ[posLin][posCol] == 0:
        #print ("Celula vazia em", posLin, posCol)
        return 1
    else:
        #print ("Celula cheia em", posLin, posCol)
        return 0
    pass

# Imprime o puzzle
def ImprimirPuzzle(PUZZ):
    print ("+-------------+")
    for a in range (0, 9):
        for b in range (0, 9):
            if b == 3 or b == 6:
                print("|", end="")
            if b == 0:
                print("| ", end="")
            if PUZZ[a][b] != 0:
                print(PUZZ[a][b], end="")
            else:
                print(" ", end="")
            if b == 8:
                print(" |", end="")
        print()
        if a == 2 or a == 5:
            print("| ---+---+--- |")
    print ("+-------------+")
    pass

def main():
    puzzleA =  [[5,3,0,0,7,0,0,0,0],
                [6,0,0,1,9,5,0,0,0],
                [0,9,8,0,0,0,0,6,0],
                [8,0,0,0,6,0,0,0,3],
                [4,0,0,8,0,3,0,0,1],
                [7,0,0,0,2,0,0,0,6],
                [0,6,0,0,0,0,2,8,0],
                [0,0,0,4,1,9,0,0,5],
                [0,0,0,0,8,0,0,7,9]]

    # http://puzzles.about.com/od/sudokupuzzles/qt/xhsodukosol01.htm
    puzzleB =  [[0,2,0,0,0,0,0,0,7,],
                [0,7,0,0,0,4,0,1,0,],
                [9,0,5,0,0,0,0,0,0,],
                [0,8,0,6,3,0,0,0,2,],
                [7,0,0,0,0,0,0,0,1,],
                [2,0,0,0,1,8,0,6,0,],
                [0,0,0,0,0,0,4,0,9,],
                [0,3,0,1,0,0,0,2,0,],
                [4,0,0,0,0,0,0,8,0,]]

    #http://www.extremesudoku.info/sudoku.html (EXTREME)
    puzzleC =  [[0,0,8,2,0,0,0,0,3,],
                [0,4,0,0,8,0,0,2,0,],
                [5,0,0,0,0,7,1,0,0,],
                [1,0,0,0,0,4,5,0,0,],
                [0,7,0,0,6,0,0,8,0,],
                [0,0,4,1,0,0,0,0,6,],
                [0,0,3,6,0,0,0,0,2,],
                [0,8,0,0,1,0,0,5,0,],
                [9,0,0,0,0,8,3,0,0,]]

    print ("Sudoku Solver (v1)")
    Resolver(puzzleC)
    pass

if __name__ == '__main__':
    main()
