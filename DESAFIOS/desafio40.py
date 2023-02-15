'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:'''

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
média = (a + b) / 2
if média < 5:
    print('Tirando {} e {}, a média do aluno é {}'.format(a, b, média))
    print('Aluno REPROVADO!!')
elif média ==5 or média < 7: # outra maneira de fazer é {elif: 7 > média >=5:}.
    print('Tirando {} e {}, a média do aluno é {}'.format(a, b, média))
    print('Aluno em RECUPERAÇÃO!!')
elif média >= 7:
    print('Tirando {} e {}, a média do aluno é {}'.format(a, b, média))
    print('Aluno APROVADO!!')
