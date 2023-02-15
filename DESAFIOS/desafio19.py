''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random
a1 = str (input('Primeiro Aluno: ')) 
a2 = str (input('Segundo Aluno: '))
a3 = str (input('Terceiro Aluno: '))
list = [a1, a2, a3]
escolha = random.choice(list)
print('O aluno sortedo foi {}'.format(escolha)) 