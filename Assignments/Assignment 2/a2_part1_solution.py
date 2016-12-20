import random

def perform_test(operation, n):
    '''(int, int)->int
    Performs a quizz
    '''
    total_correct = 0
    if operation == 0:
        print("Please give the answers to the following additions:")
        for counter in range(n): 
          num1 = random.randint(0,9)
          num2 = random.randint(0,9)  # make sure the number is never zero
          answer = int(input(str(num1) + " + " + str(num2) + " = "))
          sum = num1 + num2
          if sum == answer :
            total_correct += 1
          else: 
            print("Incorrect – the answer is ", sum)
    else:  
        print("Please give the answers to the following multiplications:")
        for counter in range(n):
          num1 = random.randint(0,9)
          num2 = random.randint(0,9)
          answer = int(input(str(num1) + " * " + str(num2) + " = "))
          mult = num1 * num2
          if(mult == answer):
            total_correct += 1
          else: 
            print("Incorrect – the answer is ", mult)
    return total_correct
    

print("Welcome to addition / multiplication test\n")
num_questions=int(input("How many questions would you like to be tested on?\n\
Enter a non negative integer for the answer: "))
if(num_questions>0):
    print("This software tests you with",  num_questions, "questions …… ");
    operation = int(input("0) Addition \n1) Multiplication\nPlease make a selection (0 or 1): "))

    total_correct = perform_test(operation, num_questions)
    percentange_correct=round(total_correct/num_questions, 2)
   
    if percentange_correct >= 0.8:
        print("Well done! Congratulations")
    elif percentange_correct >= 0.6:
        print("Not too bad but please study and practice some more.")
    else:
        print("Please study more and ask your teacher for help.")
else:
    print("Good bye")
