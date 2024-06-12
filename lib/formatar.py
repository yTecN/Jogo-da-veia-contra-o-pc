from lib.condicoes import *

class jogo():
    def __init__(self):
        self.layout = [
            [ 1 , 2 , 3 ],
            [ 4 , 5 , 6 ],
            [ 7 , 8 , 9 ]
        ]
        self.n_jogadas = 0
        self.running = True
        
    def exibe(self):
        for i1, x in enumerate(self.layout):
            print(' '*13, end='')
            for i2, y in enumerate(x):
                print(y, end='')
                print(' | ' if i2 < 2 else '\n', end='')
            print(' '*12+'-'*11 if i1 < 2 else '')
        
    def atualiza(self, jogada, jogador):
            for i1, x in enumerate(self.layout):
                for i2, y in enumerate(x):
                    if jogada == y:
                        self.layout[i1][i2] = jogador
                        self.running = False
            if self.running:
                print('Posição inválida, Tente novamente')
        
    def cabecalho(self, msg):
        print('-'*35)
        print(msg.center(35))
        print('-'*35)
        
    def jogada(self, jogador):
        print('-'*35)
        print(f'Jogador {jogador}, faça sua jogada: ')
        self.running = True
        while self.running:
            self.atualiza(valida_jogada('Pos: '), jogador)
        self.n_jogadas += 1
        print('Jogadas: ', self.n_jogadas)