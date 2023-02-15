'''Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:'''

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
if a > b:
    print('o PRIMEIRO número é maior')
elif b > a:
    print('o SEGUNDO número é maior')
else:
    print('Não existe valor maior, os dois são iguais')