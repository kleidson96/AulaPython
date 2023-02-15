'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele.'''

a = input('Digite algo: ')
print('''o tipo primitivo desse valor é {}
Só tem espaços? {}
É um número? {}
É alfabético? {}
É alfanumérico? {}
Está em maiúsculas? {}
Está em minúsculas? {}
Está captalizada? {} '''.format(type(a), a.isspace(), a.isnumeric(), a.isalpha(), a.isalnum(), a.isupper(), a.islower(),
                                a.istitle(),))