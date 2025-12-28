c=[]
for i in range(5):
    n=int(input('Digite um numero: '))
    if i==0 or n > c[-1]:
        c.append(n)
    else:
        pos=0
        while pos<len(c):
            if n<=c[pos]:
                c.insert(pos,n)
                break
            
            pos+=1
            


print(c)

