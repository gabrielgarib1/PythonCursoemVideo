
def soma_impares(n1,n2):
    res=0
    
    for c in range(n1,n2+1):
        
        if c%3==0 and c%2==1:
            res+=c
            
    print(f'a soma total de todos os e: {res}')

soma_impares(1,11)