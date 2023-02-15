'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''
nota1 = float (input('Primeira Nota do Aluno: '))
nota2 = float (input('Segnda Nota do Aluno: '))
media = (nota1 + nota2) / 2
print('a Média de {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, media ))