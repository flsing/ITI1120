
########## task 1 ################

def orange(n):
    if n > 0:
        print(n,end=" ")
        orange(n-2)

orange(10)

print()


#it prints in order 10,8,6,4,2


#riddle2

def guava(n):
    if n > 0:
        guava(n-2)
        print(n,end=" ")

guava(10)

print()

#it prints in reverse 2,4,6,8,10

########## task 2 ################

def mulberry(n):
    if n == 1:
        return 1 
    else:
      return n + mulberry(n - 1) 

print( mulberry(4) )

#it prints 10 with 4
#with -3 it is infinite

########## task 3 ################

def cantaloupe(n): 
    if n > 0:
        print( n % 10)
        cantaloupe(n // 10)     
    
cantaloupe(7254)

#pritns 4,5,2,7  on the stack there is 7254, 725, 72, 7 

########## task 4 ################
def almond(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        tmp=almond(lst[0:len(lst)-1])
        if tmp>lst[len(lst)-1]:
            return tmp
        else:
            return lst[len(lst)-1]

a = [2, 7, -11]
print( almond(a) )

#it prints 7 

########## task 5 ################
def fig(lst, high):
    if high == 0:
        return lst[0]
    else:
        tmp=fig(lst, high - 1)
        if tmp>lst[high]:
            return tmp
        else:
            return lst[high]

a = [2, 7, -11]
print( fig (a, len(a)-1) )

# it print 7

########## task 6 ################
def nox(s, ch):
    if len(s)==0:
        return s
    elif s[0]==ch:
        return nox(s[1:], ch)
    else:
        return s[0]+nox(s[1:], ch)

print( nox('Cacic', 'c' ))

#it prints cai
