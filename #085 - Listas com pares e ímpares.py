

lista=[]
pares=[]
impares=[]
for i in range(7):
    p=int(input('Digite um numero: '))
    if p%2==0:
        pares.append(p)
    else:
        impares.append(p)
lista.append(pares)
lista.append(impares)
print(f'pares em ordem crescente {sorted(lista[0])}')
print(f'impares em ordem crescente {sorted(lista[1])}')