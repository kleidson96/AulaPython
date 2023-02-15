'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
p = float (input('Qual preço de um produto? R$'))
print ('o produro que custava R${:.f}, na promoçao com desconto de 5% vai custar R${:.2f}'.format(p, p-(p*0.05)))