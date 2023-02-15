'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
seu status, de acordo com a tabela abaixo:'''
peso =  float(input('Qual seu peso?(Kg) '))
altura = float(input('Qaul sua altura?(M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!!')
elif imc < 25:
    print('Você está COM PESO NORMAL!!')
elif imc < 30 :
    print('Você está COM SOBREPESO!!')
elif imc < 40:
    print('Você está COM OBESIDADE!!')
else:
    print('Você está COM OBESIDADE MÓRBIDA')