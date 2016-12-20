def sum_odd_while_v2(n):
   odd_sum = 0
   i=5    
   while i < n: 
      if i % 2 == 1:
          odd_sum = odd_sum + i
      i=i+1 

   return odd_sum


def sum_list_while():
    ''' (list)->num
    Returns the sum of elements in a given list a'''
    answer=input("Would you like to play? ")
    while(answer == 'yes'):
           num=int(input("Please input a integer: "))
           num2=int(input("please input another integer: "))
           ans=   num+num2
           print (ans)
           answer=input("would you like to play again? ")
        
    else:
        print("Goodbye")


###not done
##def first_neg(s):
##    
##    i=0
##    while  len(s):
##        if i >0:
##            return none
##        else:
##            return s.index(i)

def sum_5_consecutive(n):
##    list_sum=0
##    for i in range (len(a)):
##        if a[1]:
##            return i 


    while [sum(n[0:i+1]) for i in range(len(n))] == 0:
        return True
    else: return False

def fib(n):
    i=0
 
    n[0]=1
    n[1]=1
    
        
 #       n[i]=a[i-1]+a[i-2]

 def inner_product():
     
    
        

