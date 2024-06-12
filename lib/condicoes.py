def valida_jogada(msg):
    while True:
        n = input(msg)
        try:
            n = int(n)
        except (TypeError, ValueError):
            print('Erro! Digite um número inteiro')
        else:
            if n > 9 or n < 1:
                print('Erro! Jogada inválida, digite um número inteiro de 1 a 9')
            else:
                return n

def verifica_vitoria(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] and linha[1] == linha[2]:
            return linha[0]
    # Verificar colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i]:
            return tabuleiro[0][i]
    # Verifica diagonais
    if (tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]) or (tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]):
            return tabuleiro[1][1]
            