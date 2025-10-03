
c=[]
par=[]
impar=[]
for i in range(5):
    c.append(int(input('Digite um numero: ')))

for num in c:
    if num % 2 ==0:
        par.append(num)
    elif num % 2==1:
        impar.append(num)

print(f'lista toda: {c}, lista de pares: {par}, lista de impares: {impar}')