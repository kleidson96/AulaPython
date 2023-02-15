''' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
d = int(input('quantos dias foi alugado? '))
k = float(input('Quantos Km rodados? '))
alg_d = 60 * d
alg_k = 0.15 * k
t = alg_d + alg_k
print('o total a pagar é de R${:.2f}'.format(t))
