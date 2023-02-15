# tempo = int(input('Quanto tempo tem seu carro? '))
# if tempo <=3:
#     print('carro novo')
# else:
#     print('carro velho')
# print('--FIM--')

#CONDIÇÃO SIMPLIFICADA#
# tempo = int(input('Quanto tempo tem seu carro? '))
# print('carro novo' if tempo <=3 else 'carro velho' )
# print('--FIM--')

#############################################
#QUANDO CONDIÇÃO NÃO TEM O ELSE É UMA ESTRUTURA CONDICIONAL SIMPLES#
# nome = str(input('Qual é seu nome? '))
# if nome == 'Kleidson':
#     print('Que nome lindo você tem!')
# print('Bom dia, {}!'.format(nome))

#############################################
#QUANDO A CODIÇÃO TEM O ELSE É UMA ESTRUTURA CONDICIONAL COMPOSTA#
# nome = str(input('Qual é seu nome? '))
# if nome == 'Kleidson':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(nome))

############################################

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) /2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')













