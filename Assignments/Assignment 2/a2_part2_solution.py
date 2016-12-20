###################################################################
# Question 1
###################################################################

def in_or_out_square(x_square, y_square, side, x_query, y_query):
     '''(number, number, number, number, number)->str

     Returns the result of a test if a query point (x_query, y_query) is
     inside of the square with bottom left corner in (x_square, y_square)
     and of given side length
     
     Precondition: all input parameters are numbers
     '''
     if side <0:
          answer="invalid side length" 
     elif (x_query>=x_square) and (x_query<=x_square+side) \
        and (y_query>=y_square) and (y_query<=y_square+side):
          answer ="The given query point ("+str(x_query)+", "+str(y_query)+") is inside of the square."
     else:
          answer ="The given query point ("+str(x_query)+", "+str(y_query)+") is outside of the square."
     return answer

###################################################################
# Question 2
###################################################################

def factorial(n):
    '''(int)->int
       Return n factorial (n!)
       Precondition: n is non negative integer
       '''
    f = 1 # note that 1 will be returned even when n=0 since when n=0 and n= 1 we do not enter the for loop
    for i in range(2,n+1):
        f *= i
    return f


###################################################################
# Question 3
###################################################################
def strange_count(s):
     '''(str)->int
         Prints the number of characters in s that meet some silly condition
     '''
     count=0
     for char in s:
          if (char>='b' and char<='s') or (char>='3' and char <='7'):
               count=count+1
     print(count)


###################################################################
# Question 4
###################################################################
def vote_percentage(results):
     '''(str)->number
     Precondition: results contains only words yes, no and abstain
     and result has at least one yes or no'''
     yes=results.count('yes')
     no=results.count('no')
     total=yes+no
     return yes/total

###################################################################
# Question 5
###################################################################
def vote():
     '''(None) -> None
     prints result of the vote
     '''
     votes=input("Enter the yes, no, abstain votes one by one and then press enter:\n ")
     yes_percentage=vote_percentage(votes)
     if yes_percentage==1.00:
          print("proposal passes unanimously")
     elif yes_percentage>=2/3:
          print("proposal passes with super majority")
     elif yes_percentage>=1/2:
          print("proposal passes with simple majority")
     else:
          print("proposal fails")
 
###################################################################
# Question 6
###################################################################
def roman():
     '''(None)->int
     Returns a decimal representation of a (simplified) roman number
     '''
     roman_num=input("Enter a roman number using capital letters M, D, C, X and I: ")
     return 1000*roman_num.count('M')+500*roman_num.count('D')\
            +100*roman_num.count('C')+10*roman_num.count('X')+5*roman_num.count('V')+roman_num.count('I')

 
###################################################################
# Question 7
###################################################################

def roman_v2():
     '''(None)->int
     Returns a decimal representation of a (simplified) roman number
     '''
     roman_num=input("Enter a roman number using capital letters M, D, C, X and I: ")
     decimal_num=0     
     for char in roman_num:
          if char=='M':
               decimal_num=decimal_num+1000
          elif char=='D':
               decimal_num=decimal_num+500
          elif char=='C':
               decimal_num=decimal_num+100
          elif char=='X':
               decimal_num=decimal_num+10
          elif char=='V':
               decimal_num=decimal_num+5
          else:
               decimal_num=decimal_num+1
     return decimal_num
  
###################################################################
# Question 8
###################################################################
def emphasize(s):
     '''(str)->str
      Returns the given string 'emphasized'
      '''
     s_emph=''
     for char in s:
          s_emph=s_emph+char+' '
     s_emph=s_emph[0:len(s_emph)-1]
     return s_emph


###################################################################
# Question 9
###################################################################
def crypto(s):
     '''(str)->str
      Returns the given string encripted
      '''
     s_crypto=''
     for i in range(0,len(s)-1,2):
          s_crypto=s_crypto+s[i+1]+s[i]
     if(len(s)%2==1): # if s of odd length, we need to add that last letter
          s_crypto=s_crypto+s[len(s)-1]
     return s_crypto


def crypto_v2(s):
     '''(str)->str
      Returns the given string encripted
      '''
     s_crypto=''
     for i in range(0,len(s),2):
          if(i< len(s)-1):
              s_crypto=s_crypto+s[i+1]+s[i]
          else: # this is only needed when len(s) is odd
               s_crypto=s_crypto+s[i]
     return s_crypto

