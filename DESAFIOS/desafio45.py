''' Crie um programa que faça o computador jogar Jokenpô com você.'''
from time import sleep
from random import randint
list = ['pedra ', 'papel', 'tesoura']
computador = randint (0, 2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 13)
print('Computador escolheu {}'.format(list[computador]))
print('Jogador escolheu {}'.format(list[jogador]))
print('-=' * 13)
if jogador == 0:
   if computador == 0:
       print('EMPATE')
   elif computador == 1:
       print('COMPUTADOR VENCEU')
   elif computador == 2:
       print('JOGADOR GANHOU')

if jogador == 1:
    if computador == 0:
        print('JOGADOR GANHOU')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('COMPUTADOR GANHOU')

if jogador == 2:
    if computador == 0:
        print('COMPUTADOR GANHOU')
    elif computador == 1:
        print('JOGADOR GANHOU')
    elif computador == 2:
        print('EMPATE')

















