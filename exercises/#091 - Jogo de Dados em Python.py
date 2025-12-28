import random as r
import time as t
d={}
for i in range(4):
    d[f'Jogador{i+1}']=r.randint(1,6)

for k,v in d.items():
    print(f'O {k} tirou {v} no dado.')
t.sleep(1)
print('== Ranking dos Jogadores ==')
#def para retornar o item na posicao 1, que sao os valores ([0] chamaria as chaves)
def element_1(item):
    return item[1]

ranking=sorted(d.items(),key=element_1, reverse=True) 

#argumento key=funcao_1 serve para determinar a chamada do [1] como parametro para ordenar 

print(ranking)
for i,v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]} no dado')
        