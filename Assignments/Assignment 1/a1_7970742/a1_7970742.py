#Family Name: Felix Singerman
#Student number: 7970742
#Course: ITI 1120
#Assignment Number 1

import math
import turtle

###################################################################
 # Question 1
 ###################################################################

def f2k(t):
    return (((t-32)*5/9)+273.15)

###################################################################
 # Question 2
 ###################################################################
    
def bibformat_apa(author,title,city,publisher,year):
    print("'"+str(author)+" " +"("+str(year)+")." +str(title)+". " +str(city)+": " +str(publisher)+".'")
     
###################################################################
 # Question 3
 ###################################################################

def joker():
    person= input("What is your name? ")
    print("Why did", person + " " + "cross the playground?")
    print("To get to the other slide")


###################################################################
 # Question 4
 ###################################################################

def bibformat_apa_display():
    title= input("What is the title of the book? ")
    author= input("Who is the author of the book? ")
    year= input("What year was the book published? ")
    publisher= input("Enter the name of the publisher: ")
    city= input("In what city are the headquarters of the publisher? ")
    bibformat_apa(author,title,city,publisher,year)
    
###################################################################
 # Question 5
 ###################################################################
def bmi(w,h):         
    w=w*0.45
    h=(h*0.025)**2
    wh=w/h
    return (wh)
          
###################################################################
 # Question 6
 ###################################################################

def f2fi(f):
    fh=math.floor(f)
    i=(f-fh)*12
    return(fh,i)

             

###################################################################
 # Question 7
 ###################################################################
 #not complete
def bmi_calculator():    
    a=input("Enter your appelation (Mr., MRs., Dr.,....): ")
    f=input("Enter your first name: ")
    l=input("Enter your last name: ")
    h=input("Enter your height in inches: ")
    w=input("Enter your weight in pounds: ")
    print("BMI Record for "+str(a)+" "+str(f)+" "+str(l))
    print("Subject is " +str(h)+" inches tall and weighs "+str(w)+" pounds")
    print("The subject's BMI is " + str(h)+str(w))


###################################################################
 # Question 8
 ###################################################################

def draw_college_court():
    
 
    t=turtle.Turtle()
    s=turtle.Screen()
                                                                               
    t.speed(0)
    t.pensize(4)
    t.pencolor("blue")

    #outline of court
    t.penup()
    t.goto(-300,-150)
    t.pendown()
    t.fillcolor("#E3DC8E")
    t.begin_fill()            
    t.right(0)
    t.forward(600)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(600)
    t.left(90)
    t.forward(300)
    t.end_fill()

    t.pensize(2)
    t.penup()
    t.goto(0,-150)
    t.pendown()
    t.right(180)
    t.forward(300)

    #middle circle
    t.penup()
    t.goto(0,-30)
    t.pendown()

    t.fillcolor("#C84646")
    t.begin_fill()
    t.right(90)
    t.circle(30)
    t.end_fill()

    t.penup()
    t.goto(0,0)
    t.dot(10)

    #semicircles
    t.penup()
    t.goto(-300,120)
    t.pendown()
    t.right(0)
    t.forward(40)
    t.circle(-120,180)
    t.forward(40)
    t.penup()
    t.goto(300,120)
    t.pendown()
    t.right(0)
    t.forward(40)
    t.circle(120,180)
    t.forward(40)

    #left freethrow

    t.fillcolor("#C84646")
    t.penup()
    t.goto(-300,-30)
    t.pendown()
    t.begin_fill()
    t.right(0)
    t.forward(100)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(100)
    t.end_fill()
    t.penup()
    t.goto(-200,-30)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.right(180)
    t.circle(30,180)
    t.end_fill()

    #right freethrow

    t.fillcolor("#C84646")
    t.penup()
    t.goto(300,-30)
    t.pendown()
    t.begin_fill()
    t.right(0)
    t.forward(100)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(100)
    t.end_fill()
    t.penup()
    t.goto(200,-30)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.right(180)
    t.circle(-30,180)
    t.end_fill()

    #basket

    t.penup()
    t.goto(270,-5)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(275,0)
    t.pendown()
    t.pensize(3)
    t.forward(4)
    t.left(90)
    t.forward(15)
    t.left(180)
    t.forward(30)

    t.penup()
    t.pensize(2)
    t.goto(-270,0)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(-270,0)
    t.pendown()
    t.pensize(3)
    t.left(270)
    t.forward(4)
    t.left(90)
    t.forward(15)
    t.left(180)
    t.forward(30)

    #lines left bottom
    t.penup()
    t.goto(-260,-33)
    t.pendown()
    t.right(180)
    t.pensize(6)
    t.forward(4)
    
    t.penup()
    t.goto(-245,-31)
    t.pendown()
    t.pensize(3)
    t.forward(4)

    t.penup()
    t.goto(-230,-31)
    t.pendown()
    t.forward(4)

    t.penup()
    t.goto(-215,-31)
    t.pendown()
    t.forward(4)
#line left top
    t.penup()
    t.goto(-260,33)
    t.pendown()
    t.right(180)
    t.pensize(6)
    t.forward(4)

    t.penup()
    t.goto(-245,31)
    t.pendown()
    t.pensize(3)
    t.forward(4)

    t.penup()
    t.goto(-230,31)
    t.pendown()
    t.forward(4)

    t.penup()
    t.goto(-215,31)
    t.pendown()
    t.forward(4)

    #line right top

    t.penup()
    t.goto(260,33)
    t.pendown()
    t.pensize(6)
    t.forward(4)

    t.penup()
    t.goto(245,31)
    t.pendown()
    t.pensize(3)
    t.forward(4)

    t.penup()
    t.goto(230,31)
    t.pendown()
    t.forward(4)

    t.penup()
    t.goto(215,31)
    t.pendown()
    t.forward(4)

    #line right bottom

    t.penup()
    t.goto(260,-33)
    t.pendown()
    t.right(180)
    t.pensize(6)
    t.forward(4)
    
    t.penup()
    t.goto(245,-31)
    t.pendown()
    t.pensize(3)
    t.forward(4)

    t.penup()
    t.goto(230,-31)
    t.pendown()
    t.forward(4)

    t.penup()
    t.goto(215,-31)
    t.pendown()
    t.forward(4)

    t.penup()
    t.goto(100000,10000)


###################################################################
 # Question 9
 ###################################################################
 
def forms_triangle(a,b,c):
    print(a<=b+c and b<=a+c and c<=a+b)
    


###################################################################
 # Question 10
 ###################################################################    

def change_to_coins(amount):
    p=1
    n=5
    d=10
    q=25
    sa=math.ceil(amount*100)
    sq=math.floor(sa/q)
    sb=(sa-(sq*q))
    sd=math.floor(sb/d)
    sc=(sb-(sd*d))
    sn=math.floor(sc/n)
    sz=(sc-(sn*n))
    sp=math.floor(sz/p)
    return sq+sd+sn+sp

    
    
