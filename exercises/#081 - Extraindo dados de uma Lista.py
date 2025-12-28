
c=[]
for i in range(5):
    n=int(input('digite um numero: '))
    c.append(n)
print(f'Foram digitados {len(c)} numeros')
print(f'A lista em ordem decrescente e: {sorted(c,reverse=True)}')
if 5 in c:
    print('O numero 5 foi digitado')