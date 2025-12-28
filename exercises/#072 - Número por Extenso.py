

cont= ('zero','um','dois','tres','quatro','cinco','seis',
       'sete','oito','nove','dez')


while True:
    num= int(input('digite um numero de 0 a 10: '))
    if 0<=num<=10:
        break
    print('Tente Novamente')
print(f'Voce digitou o numero {cont[num]}')