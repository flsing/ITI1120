import math
import turtle



      
          
def bmi(w,h):         
    w=(w*0.45)
    h=((h*0.025)**2)
    wh=(w/h)
    return (wh)


def bmi_calculator():
    a=input("Enter your appelation (Mr., MRs., Dr.,....): ")
    f=input("Enter your first name: ")
    l=input("Enter your last name: ")
    h=input("Enter your height in inches: ")
    w=input("Enter your weight in pounds: ")      
    print("BMI Record for "+str(a)+" "+str(f)+" "+str(l))
    print("Subject is " +str(h)+" inches tall and weighs "+str(w)+" pounds")
    print("The subject's BMI is " + str(bmi(str(w),str(h))))


