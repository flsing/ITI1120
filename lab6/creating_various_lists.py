import random

n=int(input("Enter a positive even integer for the size of the list?" ))

# 1
a = [0]*n
print(a)

a=[]
for i in range(n):
    a=a+[0]
print(a)
    

#2
random= random.sample(range(1, 100), n)
b= [random]
print(b)

b=[None]
for i in range (n):
    b=b+[random.randint(1,1000)]
print(b)
    


#3
c=b

#4
c=len(c)/2*0+c

for i in range(len(c)//2):
    c[i]=0
print(c)
print(b)

#5
d=b[:]

d=[]
for i in range (len(b)):
    d=d+[b[i]]
print(d)

#6

e=[]
for i in range(0,len(b),2):
    e=e+[b[i]]
print(e)

