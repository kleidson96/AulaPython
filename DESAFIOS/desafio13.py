''' Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

s = float (input('Qual é o salário do funcionário? R$'))
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passar a receber R${:.2f}'.format(s, s+(s*0.15)))