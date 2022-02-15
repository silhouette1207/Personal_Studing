#Sieve of Eratosthenes

def Eratosthenes(n):
    
    answer = [True] *n
    
    p = int(n**0.5)
    
    for i in range(2,p+1):
        if answer[i] == True:
            for j in range(i+j,n,i):
                answer[j]=False
    
    return [i for i in range(2,n) if answer[i] == True]
    
    


num = int(input("Max Number : "))

print(Eratosthenes(num))







