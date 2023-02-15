'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
print('-=-' * 20)
print('\033[4mAnalizador de Triângulos\033[m')
print('-=-' * 20)
a = float(input('\033[m Primeiro segmento: \033[m'))
b = float(input('\033[mSegundo segmento: \033[m'))
c = float(input('\033[mTerceiro segmento: \033[m'))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo!')
