'''Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''
n = str (input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(n.upper()))
print('Seu nome em minúscula é {}'.format(n.lower()))
print('Seu nome tem ao todo {}'.format(len(n)-n.count(' ')))
#print('Seu primeiro nome  tem {} letras'.format(n.find(' ')))
separa = n.split()
print('Seu primeiro nome é {} e ele tem {} lentras'.format(separa[0], len(separa[0])))
