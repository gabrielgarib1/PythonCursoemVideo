
print('digite numeros em ordem para formar uma matriz.')
matriz=[
        [],
        [],
        []
        ]
for i in range(3):
    for j in range(3):
        matriz[i].append(input('Digite:'))
        print(matriz)
print('M=',end='')
for l in range(3):
    print('    ',matriz[l])
