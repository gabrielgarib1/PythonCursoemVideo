
a=int(input('Digite um numero:'))
b=int(input('Digite um numero:'))
c=int(input('Digite um numero:'))
d=int(input('Digite um numero:'))

tup=(a,b,c,d)
print(f'num 9 apareceu {tup.count(9)} vezes.')
if 3 in tup:2\
    print(f'O primeiro tres aparece na posicao {tup.index(3)+1}')
par=[]
for t in tup:
    if t%2==0:
        par.append(t)
print(f'os pares foram {par}')