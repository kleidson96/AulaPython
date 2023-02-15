'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

#import math
#n = float (input('Digite um valor: '))
#print('o Valor digitado foi {} e sua proporção inteira é #{}'.format(n, math.trunc(n) 

######### OU DESSA MANEIRA#######

from math import trunc
n = float (input('Digite um valor: '))
print('o Valor digitado foi {} e sua proporção inteira é {}'.format(n, trunc(n)))


