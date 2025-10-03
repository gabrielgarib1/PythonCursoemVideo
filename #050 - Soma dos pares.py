res=0
num=0
for i in range(6):
    n=int(input(f'digite o {i+1} numero: '))
    if n%2==0:
        res+=n
        num+=1

print('a soma de ',num, 'PARES e igual a ',res)