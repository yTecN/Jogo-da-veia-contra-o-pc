from lib.formatar import *
from lib.condicoes import *
from lib.cerebro import *
from time import sleep
import os

jogo = jogo()

jogo.cabecalho('Escolha seu jogadorolo')
print('''
[ 1 ] X
[ 2 ] O
''')
while True:
    try:
        jogador = int(input('Sua escolha: '))
    except (TypeError, ValueError):
        print('Digite um número inteiro!!!')
    else:
        if jogador in (1, 2):
            break
        else:
            print('Selecione uma opção válida!!!')
if jogador == 1:
    jogador = 'X'
    pc = 'O'
else:
    jogador = 'O'
    pc = 'X'

jogo.cabecalho('Jogo da Veia')
jogo.exibe()

while True:
    if verifica_vitoria(jogo.layout) or jogo.n_jogadas >= 9:
        break
    if jogador == 'X':
        ordem = (jogador, pc)
    else:
        ordem = (pc, jogador)
    for j in ordem:
        if j == pc:
            print(f'Vez do PC...')
            sleep(1.5)
            pc_jogada = jogada_pc(jogo.layout, pc, possiveis_jogadas(jogo.layout))
            jogo.atualiza(pc_jogada, j)
            jogo.n_jogadas += 1
        else:
            try:
                if pc_jogada in range(1, 10):
                    print(f'Jogada do pc: {pc_jogada}')
            except:
                pass
            jogo.jogada(j)
        os.system('cls')
        jogo.cabecalho('Jogo da Veia')
        jogo.exibe()
        if verifica_vitoria(jogo.layout) or jogo.n_jogadas >= 9:
            break

if verifica_vitoria(jogo.layout):
    jogo.cabecalho('Vitória do pc' if verifica_vitoria(jogo.layout) == pc else 'Vitória do jogador')
else:
    jogo.cabecalho('Empate')