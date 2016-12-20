def is_eligible(age,citizenship,prison):
     citizenship = citizenship.lower()
     prison = prison.lower()
     if age >=18 and (citizenship== ("Canadian") or citizenship==("Canada") or citizenship==("canada")) and (prison==("No")):
          return True
     else:
          return False
     

     
     
name=input("What is your name? ")
age= int(input("How old are you? "))
citizenship=str(input("What is your citizenship? "))
prison=str(input("Are you currently in prison? "))

if is_eligible(age,citizenship,prison):
     print(name, ", you are eligible to vote")
else:
     print(name, ", you are ineligible to vote") 
    



          
