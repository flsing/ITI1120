def m(i):

    i/(2*i+1)
    return 


def count_digits(n):

    if n < 10:
        return 1
    else:
        return 1 + count_digits(n/10)



def is_palindrome(s):

    if len(s)<=1:
        return True
    
    else:
        if ((s[0]) == (s[len(s)-1])):
            return is_palindrome(s[1:len(s)-1])
            
        else:
            return False

