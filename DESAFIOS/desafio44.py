'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:'''
#print('='* 12, 'LOJAS KLEIDSON', '=' * 12)
print('{:=^40}'.format(' LOJAS KLEIDSON ')) #Guanabara fez assim
preco = float(input('Qual preço das compras? R$ '))

print('\33[31mFORMAS DE PAGAMENTO\33[m')
print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão')
[ 3 ] 2x no cartão')
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra  vai custar 2 parcela de R${} sem juros'.format( parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada de {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))







