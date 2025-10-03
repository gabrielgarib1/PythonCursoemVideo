
aluno1=input('Nome do aluno: ')
media1=float(input('Media do aluno: '))
d={'aluno':aluno1,'media':media1}
print('-='*50)

if d['media']>=7:
    d['situacao']='aprovado'
elif 5<=d['media']<7:
    d['situacao']='em recuperacao'
else:
    d['situacao']='reprovado'

for k,v in d.items():
    print(f'{k}: {v}')
          
