
def linha():
    print('-='*15)

brasileirao= ('Botafogo','Palmeiras','Flamengo','Atletico-MG','Fluminense','Gremio',
              'Athletico-PR','Sao Paulo','Cruzeiro','Internacional',
              'Fortaleza','Bragantino','Santos','Cuiaba','Corinthians','Goias','America-MG',
              'Vasco','Coritiba')

linha()
print(f'Os cinco primeiros: {brasileirao[:6]}')
linha()
print(f'Os rebaixadoss: {brasileirao[-4:]} ')
linha()
print(f'Em ordem alfabetica: {sorted(brasileirao)}')
linha()
print('O Flamengo esta na posicao', brasileirao.index('Flamengo'))