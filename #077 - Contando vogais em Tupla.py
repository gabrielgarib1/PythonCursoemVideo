

tup=('pokemon','temos','que','pegar','isso','eu','sei')
for n in tup:
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')