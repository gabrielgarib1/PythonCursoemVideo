
frase=input('Digite uma frase com os parentesis corretamente: ')
pilha=[]

for w in frase:
    if w=='(':
        pilha.append('(')
    elif w==')'and len(pilha)>0:
        pilha.pop()
    else:
        pilha.append(9)
if len(pilha)==0:
    print('Frase corretamente parentada')
else:
    print('Faltam parentesis')

