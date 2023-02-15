'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''
d = float (input('Qaunto dinheiro você tem na carteira? R$'))
print('Com R${} você pode comprar US${:.2f}'.format(d, d/3.27))