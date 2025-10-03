
d={}
d['jogador']=input('nome do jogador: ')
partidas=int(input('Quantas partidas o jogador jogou: '))
ngols=[]
tot=0
for i in range(partidas):
    gol=int(input(f'quantos gols fez na partida {i+1}? '))
    tot+=gol
    ngols.append(gol)

d['gols']=ngols
d['total']=tot
print('-='*50)
print(d)
print('-='*50)

for k,v in d.items():
    print(f'{k} : {v}')

print('-='*50)
print(f'O jogador {d["jogador"]} jogou {partidas} partidas ')
for i,v in enumerate(d['gols']):
    print(f'Na partida {i+1}, fez {v} gols')