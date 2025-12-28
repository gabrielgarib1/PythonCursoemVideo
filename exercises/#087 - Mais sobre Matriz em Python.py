
print('digite numeros em ordem para formar uma matriz.')
matriz=[
        [],
        [],
        []
        ]
resl=0
restot=0
ter=0
for i in range(3):
    for j in range(3):
        e=int(input('Digite:'))
        matriz[i].append(e)
        if e%2==0:
            resl+=e
        
    
print('M=',end='')
for l in range(3):
    print('    ',matriz[l])
for k in range(3):
    ter+=matriz[k][2]


print(f'Soma de todos os elementos pares eh: {resl}')
print(f'A soma dos elementos da terceira coluna eh: {ter}')
print(f'O maior elemento da segunda linha eh: {max(matriz[1])}')



