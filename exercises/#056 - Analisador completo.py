midade=0
s_idades=0
m20menos=0
for i in range(1):
    print('---',i+1,'ª Pessoa ---\n')

    nome=input('Nome: ')
    idade=int(input('Idade:'))
    sexo=input('Sexo[M/F]: ')

    s_idades+=idade
    if sexo in 'Mm' and idade>midade:
        velho=nome
        midade=idade
    if sexo in 'Ff' and idade<=20:
        m20menos+=1

print('Media das idades:',s_idades/(i+1))
print(f'O homem mais velho tem {midade} anos e se chama {velho}')
if m20menos ==1:
    print('Uma Mulher tem menos de 20 anos')
if m20menos >1:
    print(f'Ao todo sao {m20menos} com menos de 20 anos')