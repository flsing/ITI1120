###################################################################
# Question 1
###################################################################

def in_or_out_square(xbottomleft,ybottomleft,side,xquery,yquery):
    '''(int),(int),(int),(int),(int)->str
    Returns weather or not the x query and yquery point is in the square made up of the sides
    from xbottomleft point and ybottomleft point.
    '''
 
    if side<0:
        return "invalid side length"
    elif (xquery-xbottomleft)**2 + (yquery-ybottomleft)**2 < side**2:
        return "The given query point ("+ str(xquery) +", "+ str(yquery) +") is inside the square."
    else:
        return "The given query point ("+str(xquery) + ", " + str(yquery) +") is outside the square."



###################################################################
# Question 2
###################################################################

def factorial(n):
    '''(int)->int
    Returns the factorial of n assuming n is a non-negative integer.
    '''
    factorial=1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            factorial=factorial*i
        return factorial



###################################################################
# Question 3
###################################################################

def strange_count(s):
    '''(str)->int
    Returns the number of target letters and numbers in a given string.
    '''
    num_of_char=0
    for x in s:
        if x in "bcdefghijklmnopqrs34567":
             num_of_char=num_of_char+1
    return num_of_char     


    
###################################################################
# Question 4
###################################################################

def vote_percentage(results):
    '''(str)->float
    Returns the percentage of yes voters to no voters from the results.
    '''
    num_yes=results.count("yes")
    num_no=results.count("no")

    return num_yes/(num_yes+num_no)
            
        
            
###################################################################
# Question 5
###################################################################

def vote():
    '''(str)->str
    Prints the outcome of the vote. If unanimous, it passes "unanimously", if at least 2/3
    are yes then "super majority", and if at least 1/2 are yes then "simple majority
    Function makes call to vote_percentage.
    '''

    results=(input("Enter the yes, no, abstained, votes one by one and then press enter: "))
    if vote_percentage(results) == 3/3:
        print("proposal printed unanimously")
    elif vote_percentage(results) >=2/3  :
        print("proposal passes wth super majority")
    elif vote_percentage(results) >=1/2  :
        print("proposal passes with simple majority")
    else:
        print("proposal fails")
        

    
###################################################################
# Question 6
###################################################################
def roman():
    '''(str)->int
    Returns the users input string of Roman numerals using python's functions/methods uncluding
    dot operators by counting each time they appear in the string multiplied by its value.
    Adding all values of Roman numerals using a simple version of Roman numerals where we
    just accumulate the values of all symbols.
    '''
    M=1000
    D=500
    C=100
    X=10
    V=5
    I=1

    rnum=(input("Enter a roman number using capital letters M,D,C,X and I: "))

    M=(rnum.count("M")*M)
    D=(rnum.count("D")*D)
    C=(rnum.count("C")*C)
    X=(rnum.count("X")*X)
    V=(rnum.count("V")*V)
    I=(rnum.count("I")*I)
    return M+D+C+X+V+I



###################################################################
# Question 7
###################################################################     

def roman_v2():
    '''(str)->int
    Returns the users input string of Roman numerals without using python's functions/methods
    by using for loops each time they appear in the string multiplied by its value.
    Adding all values of Roman numerals using a simple version of Roman numerals where we
    just accumulate the values of all symbols.
    '''
    num_of_M=0
    num_of_D=0
    num_of_C=0
    num_of_X=0
    num_of_V=0
    num_of_I=0
    
    rnum=(input("Enter a roman number using capital letters M,D,C,X and I: "))
    
    for char in rnum:
        if char in 'M':
            num_of_M=num_of_M+1
        if char in 'D':
            num_of_D=num_of_D+1
        if char in 'C':
            num_of_C=num_of_C+1
        if char in 'X':
            num_of_X=num_of_X+1
        if char in 'V':
            num_of_V=num_of_V+1
        if char in 'I':
            num_of_I=num_of_I+1
            
    return num_of_M*1000+ num_of_D*500+num_of_C*100+num_of_X*10+num_of_V*5+num_of_I*1



###################################################################
# Question 8
################################################################### 

def emphasize(s):
    '''(str)->str
    Returns a string with a blank space between ever pair of consecutive characters from the string
    '''
    s=s.replace(""," ")
    return s.strip()




###################################################################
# Question 9
################################################################### 
def crypto(s):
    '''(str)->str
    Returns an encrypted string that splits up the text into blocks and swap each pair of letters
    '''
  
    s=[s[i:i + 2] for i in range(0, len(s), 2)]
      
 
    list.reverse(s)

    
    return s





    
