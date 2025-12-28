from datetime import datetime
d={}
d['nome']=input('Nome: ')
d['nasc']=int(input('Ano de nascimento: '))
d['idade']=datetime.now().year -d['nasc']
temcarta=input('Tem carteira de trabalho [S/N]')
if temcarta in 'sS':
    d['carteiradetrabalho']=input('Numero da carteira de trabalho: ')
    d['anocontratacao']=int(input('Ano de contratacao: '))
    d['salario']=float(input('Salario: R$'))
    d['anoaposentadoria']= f'{d["anocontratacao"]+35 - d["nasc"]} anos'
print('-='*40)
for k,v in d.items():
    print(f'{k} : {v}')
