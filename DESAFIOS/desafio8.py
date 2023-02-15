'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
Aula Anterior'''
n = float (input('uma distancia e metros: '))
print('a medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n, n/1000, n/100, n/10, n*10, n*100, n*1000))

