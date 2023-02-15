'''ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. PERGUNTE O
VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PGAR. A PRESTAÇÃO MENSAL, NÃO EXCEDER
30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.'''

#dados do empréstimo
casa = float(input('Qual valor da casa? '))
salario = float(input('Qual o salario do comprador? '))
ano = float(input('Em quantos anos seram pagos? '))
#cálculo do empréstimo
parcela = casa / (ano * 12)
mínimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, ano, parcela))
if parcela <= mínimo:
    print('Empréstimo CONCEDIDO!!')
else:
    print('Empréstimo NEGADO!!')


