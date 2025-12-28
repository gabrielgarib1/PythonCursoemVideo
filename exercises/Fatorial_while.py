

def fatorial(n):
    
    if n==0 or n==1:
        return 1
    elif n<0 or type(n)==float:
        return 'invalid number'
    res=1
    while n>1:
        fat=n*(n-1)
        res*=fat
        
        n-=2
    return int(res)


x=fatorial(0)
print(x)