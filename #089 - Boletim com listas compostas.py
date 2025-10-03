import time 
data=[]
aluno=[]
media=[]
while True:
    aluno.append(input('Nome do aluno: '))
    aluno.append(int(input('Nota da primeira prova: ')))
    aluno.append(int(input('Nota da segunda prova: ')))
    data.append(aluno[:])
    media.append((aluno[1]+aluno[2])/2)
    aluno=[]
    
    resposta=input('Quer continuar a cadastrar alunos?  [S/N] ')
    if resposta in 'Nn':
        break
print('-='*30)
for i in range(len(data)):
    print(f'{data[i][0]}:                   {media[i]}')
print('-='*30)
time.sleep(1)
while True:
    a=input('Deseja verificar as notas de algum dos alunos? [S/N]')
    if a in'Nn':
        break
    if a in 'Ss':
        b=input('De qual aluno deseja verificar? ')
        for i in range(len(data)):
            if b in data[i][0]:
                print(f'notas do {data[i][0]} sao: {data[i][1:]}')
    else:
        print('Digite uma resposta valida.')    
    time.sleep(1)
