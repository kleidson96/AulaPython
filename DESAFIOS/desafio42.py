'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:'''

a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmeno: '))
c = float(input('Terceiro Segmento: '))

if a < b + c and b < a + c and c < b + a:
    print('Os segmentos podem formar um triângulo', end=' ')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')

else:
    print('Os segmentos não podem formar um triângulo')

