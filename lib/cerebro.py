def possiveis_jogadas(tabuleiro):
    pos_disp = []
    for linha in tabuleiro:
        for pos in linha:
            if pos in range(1, 10):
                pos_disp.append(pos)
    return pos_disp

def jogada_pc(tabuleiro, pc, pos_disp=[]):
    from random import randint, choice
    if pc == 'O':
        player = 'X'
    else:
        player = 'O'
    if len(pos_disp) == 9:
        return randint(1, 9)
    else:
        opc = []
        # Verifica linhas
        for linha in tabuleiro:
            if linha[0] in range(1, 10):
                if linha[1] in (pc, player) and linha[1] == linha[2]:
                    opc.append(linha[0])
            elif linha[1] in range(1, 10):
                if linha[0] in (pc, player) and linha[2] == linha[0]:
                    opc.append(linha[1])
            elif linha[2] in range(1, 10):
                if linha[1] in (pc, player) and linha[0] == linha[1]:
                    opc.append(linha[2])
        # Verifica colunas
        for i in range(3):
            if tabuleiro[0][i] in range(1, 10):
                if tabuleiro[1][i] in (pc, player) and tabuleiro[2][i] == tabuleiro[1][i]:
                    opc.append(tabuleiro[0][i])
            elif tabuleiro[1][i] in range(1, 10):
                if tabuleiro[0][i] in (pc, player) and tabuleiro[2][i] == tabuleiro[0][i]:
                    opc.append(tabuleiro[1][i])
            elif tabuleiro[2][i] in range(1, 10):
                if tabuleiro[1][i] in (pc, player) and tabuleiro[0][i] == tabuleiro[1][i]:
                    opc.append(tabuleiro[2][i])
        # Verifica Diagonais
        if tabuleiro[1][1] in range(1, 10):
            if (tabuleiro[0][0] in (pc, player) and tabuleiro[2][2] == tabuleiro[0][0]) or (tabuleiro[0][2] in (pc, player) and tabuleiro[2][0] == tabuleiro[0][2]):
                opc.append(tabuleiro[1][1])
        else:
            if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[2][0] in range(1, 10):
                opc.append(tabuleiro[2][0])
            elif tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[2][2] in range(1, 10):
                opc.append(tabuleiro[2][2])
            elif tabuleiro[2][2] == tabuleiro[1][1] and tabuleiro[0][0] in range(1, 10):
                opc.append(tabuleiro[0][0])
            elif tabuleiro[2][0] == tabuleiro[1][1] and tabuleiro[0][2] in range(1, 10):
                opc.append(tabuleiro[0][2])

        print(f'{opc=}')
        if len(opc) == 0:
            return choice(pos_disp)
        else:
            return choice(opc)
# debug
if __name__ == '__main__':
    layout = [
        [ 'X' , 2 , 'X' ],
        [ 4 , 'O' , 6 ],
        [ 7 , 8 , 'X' ]
    ]
    print(f'{possiveis_jogadas(layout)=}')
    print(pc_jogada(layout, 'O', possiveis_jogadas(layout)))
