'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
# sorteio = random.randrange(5)+1
# #print(sorteio)
# user = int(input('Qual numero o computador escolheu? '))
# if user == sorteio:
#     print('PARABÉNS! Você acertou!')
# else:
#     print('Infelismente você errou!')

#####################################################################
# list= [0,1,2,3,4,5]
# sorteio = random.choice(list)
# list2 = ['vc errou', 'tente novamete', 'deu ruim', 'vc cagou', 'nao foi dessa vez']
# sorteio2 = random.choice(list2)
# print(sorteio)
# user = int(input('Qual numero o computador escolheu? '))
# if user == sorteio:
#     print('PARABÉNS! Você acertou!')
# else:
#     print(sorteio2)
#######################################################################

# sorteio = random.randrange(5)+1
# #print(sorteio)
# user = int(input('Qual numero o computador escolheu? '))
# if user == sorteio:
#     print('PARABÉNS! Você acertou!')
# elif user < sorteio:
#     print('seu numero é menor que o escolhido!')
# elif user > sorteio:
#     print('seu numero é maior que o escolhido')
#########################################################################

#DO JEITO QUE GUANABARA FEZ#
from random import randint
from time import  sleep
computador = randint (0, 5) #faz o computador "PENSAR"

print('\033[4;30;45m-=-\033[m' * 20)

print('\033[0;36mVou pensar em um número entre 0 e 5. tente advinhar...')

print('\033[4;30;45m-=-\033[m' * 20)

jogador = int(input('\033[0;33mEm que numero eu pensei? ')) # Jogador tenta adivinhar

print('\033[0;33m PROCESSANDO...')

sleep(3)

if jogador == computador:
    print('\033[0;32m PARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[0;31m GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))




















