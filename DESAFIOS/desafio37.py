''' Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
conversao = int(input('Sua opção: '))
if conversao == 1:
    print('{} Convertido para Binário é igual a {}'.format(n, bin(n)[2:]))
elif conversao == 2:
    print('{} Convertido para Octal é igual a {}'.format(n, oct(n)[2:]))
elif conversao == 3:
    print('{} Convertido para Exadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('opção invalida tente novamente!')

