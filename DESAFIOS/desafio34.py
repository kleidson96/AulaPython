'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

Aula Anterior
V'''

salario = float(input('Qual o salario? '))

if salario <= 1.250:
    almento = salario + (salario * 15 / 100)
else:
    almento = salario + (salario * 10 / 100)
    print('O aumento de salário é {}'.format(almento))