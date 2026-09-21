print('Bem vindo ao sistema de chamados, para abrir um, preencha os campos abaixo: ')

simOuNao = str(input('deseja abrir um chamado? '))
contadDeCham = 0
chamBaiPrio = 0
chamMedPrio = 0
chamAltPrio = 0

while simOuNao == 'sim':
    contadDeCham += 1
    nomeDofunc = str(input('Qual seu nome? '))
    tipDeProb = int(input('Qual o tipo do seu problema? 1- computador, 2- internet, 3- sistema, 4- impressora: '))
    descDoProb = str(input('Faça uma breve descrição do seu problema: '))
    grauDoProb = int(input('Qual o grau de urgência? \n'
                           '1- baixa: não interfere significativamente no trabalho, \n'
                           '2- média: prejudica, mas não impede o trabalho, \n'
                           '3- alta: impede completamente o funcionário de trabalhar: '))

    if grauDoProb == 1:
        chamBaiPrio += 1
    elif grauDoProb == 2:
        chamMedPrio += 1
    elif grauDoProb == 3:
        chamAltPrio += 1

    print(f'\nchamado registrado:')
    print(f'nome do funcionário: {nomeDofunc}')
    print(f'tipo do problema: {tipDeProb}')
    print(f'desc do problema: {descDoProb}')
    print(f'grau do problema: {grauDoProb}')

    simOuNao = str(input('deseja abrir mais um chamado? '))

print('\nfinalizando...')
print(f'chamados registrados: {contadDeCham}')
print('suas devidas prioridades: ')
print(f'chamados de baixa urgência: {chamBaiPrio}')
print(f'chamados de média urgência: {chamMedPrio}')
print(f'chamados de alta urgência: {chamAltPrio}')