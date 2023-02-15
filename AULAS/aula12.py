nome = str (input('Qual é seu nome? '))
if nome == 'Kleidson':
    print('Que nome bonito!')
elif nome == 'predro ' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bom popular no Brasil.')
elif nome in 'ana claudia jessica juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))