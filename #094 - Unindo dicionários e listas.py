
d={}
pessoas=[]
soma=0
acimadamedia=[]
while True:
    d['nome']=input('nome: ')
    while True:
        d['sexo']=input('sexo [M/F]: ')
        if d['sexo'] in 'MFmf':
            break
        print('somente masculino e feminino.')
    d['idade']=int(input('idade: '))
    soma+=d['idade']
    pessoas.append(d.copy())
    d.clear()
    res=input('Qier continuar? [S/N]')
    if res in 'Nn':
        break

print(f'1- tem {len(pessoas)} pessoas cadastradas')

media=soma/len(pessoas)
print(f'2- a media de idade e {media:5.2f} anos')
print('3- as mulheres sao ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(p['nome'],end=', ')
print()
for p in pessoas:
    if p['idade']>media:
        acimadamedia.append(p['nome'])
print('pessoas com idade acima da media: ',end='')
for o in acimadamedia:
    print(o,end=', ')


