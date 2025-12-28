
c=[]
for v in range(5):
    a=int(input('Digite um valor '))
    c.append(a)
j=''
k=''
for i,v in enumerate(c):
    if v==max(c):
        aaa=f'{i}, '
        j+=aaa
    if v==min(c):
        aa=f'{i}, '
        k+=aa
print(f'o maximo e: {max(c)} na posicoes {j}')
print(f'o minimo e: {min(c)} na posicoes {k}')

