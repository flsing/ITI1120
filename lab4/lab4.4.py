
    
def prime(num):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                return False
            
        return True

def divisor (num):
    for i in range(1, num//2+1):
        if num%i==0:
            print(i)
    

num=int(input("Please give me a positive int: "))



#print("The " + num, +"is a prime")        
                

    
