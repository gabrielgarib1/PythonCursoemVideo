
c=[]

while True:
    
    v=int(input('Digite um numero: '))
    if v not in c:
        c.append(v)

    if len(c)==5:
        break
    
print(f'Lista dos numeros em ordem crescente{sorted(c)}')

