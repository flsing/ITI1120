import random

def perform_test():
 



    
    if (n==0):
        print ("Good bye")
    else:
        print("This software tests you with", n, "questions .....")
        print("0) Addition")
        print("1) Multiplication")

        am=int(input("Please make a selection (0 or 1): "))

        if am == 0:
               correct_ans=0

        first=int(input("5+2 :"))
        if first ==7:
            correct_ans=correct_ans+1
            print("Correct")
            return correct_ans   
        else:
            print("Incorrect - the answer is 7")
 
   
            
print("Welcome to addition / multiplication test" )
print("How many questions would you like to be tested on?")
n=int(input("Enter a non negative integer for the answer: "))
perform_test()

    
