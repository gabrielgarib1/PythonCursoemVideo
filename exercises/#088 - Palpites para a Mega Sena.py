
from random import*
jogo=[]
njogos=int(input('Quantos jogos voce quer que sorteie ? '))
for j in range(njogos):
    while True:
        num=randint(1,60)
        if num not in jogo:
            jogo.append(num)
        if len(jogo)==6:
            break
    print(f'Jogo{j+1}: {sorted(jogo)}')
    jogo.clear()
