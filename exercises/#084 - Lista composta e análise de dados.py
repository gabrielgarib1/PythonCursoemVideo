
pessoas=[]
data=[0,0]
pesos=[]
for i in range(3):
    data[0]=input('Digite nome: ')
    data[1]=input('Digite peso: ')
    pessoas.append(data[:])

print(f'foram cadastradas {len(pessoas)}')
for dados in pessoas:
    print(f'Pessoas pesadas: {dados[0]}')
for dados2 in pessoas:
    pesos.append(dados2[1])
print(sorted(pesos))