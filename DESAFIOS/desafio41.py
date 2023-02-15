'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:'''

from datetime import date
ano = date.today().year
n = int(input('Qual ano de nascimento: '))
idade = ano - n
print('O atelta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM.')
elif idade <=14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação: JÚNIOR.')
elif idade <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classificção: MASTER.')