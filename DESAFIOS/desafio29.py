''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

# velocidade = float(input('\033[0;36mQual velocidade do carro? \033[m'))
# multa = velocidade - 80
# if velocidade > 80:
#      print('\033[0;31m Você foi Multado!')
#      print('o valor de sua multa é R${:.1f}'.format(7*multa))
# else:
#      print('\033[0;32m Você não foi multado!')


#DO JEITO QUE GUANABARA FEZ#

velocidade = float(input('Qual velocidade do carro? '))
if velocidade > 80:
     print('MULTADO! Você excedeu o limite permitido que é de 80km/hr')
     multa= (velocidade - 80) *7
     print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
