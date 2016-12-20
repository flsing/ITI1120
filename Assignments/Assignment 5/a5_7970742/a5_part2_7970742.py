


def largest_two(a):
    '''lst->int
    Return the sum of the two largest items in the lsit.
    '''

    largest=sorted(a)[-1]
    second=sorted(a)[-2]
    
    return largest+second


def smallest_half(a):
    '''lst->int
    returns the sum on half of the list that contains the smallest numbers
    '''
    suml=0
    newlst=sorted(a)
    newlst=newlst[:len(a)//2]

    for i in newlst:
        suml=suml+i
    return suml


def median(a):
    '''lst->num
    return median of list
    '''
    sorteda = sorted(a)
    aLen = len(a)
    index = (aLen - 1) // 2

    if (aLen % 2):
        return sorteda[index]
    else:
        return (sorteda[index] + sorteda[index + 1])/2.0


def at_least_third(a):
    '''lst->int or None
    returns a value that occurs at least len(a)//3+1 times, if not then returns
    false
    '''
    
    newlst=sorted(a)//3+1
    i=0
    
    for i in range(len(newlst)):
        i=i+1
        return i


##def triple_sum(a,x)
##    '''(lst,
