''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.Aula Anterior'''

import math
ag = float (input('Digite o angulo que você deseja: '))
print('o angulo de {} tem o Seno de {:.2f}'.format(ag, math.sin(math.radians(ag)) ))
print('o angulo de {} tem o Cosseno de {:.2f}'.format(ag , math.cos(math.radians(ag))))
print('o angulo de {} tem a Tangente de {:.2f}'.format(ag, math.tan(math.radians(ag))))