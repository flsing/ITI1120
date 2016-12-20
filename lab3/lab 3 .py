#question 1

def pay(w,h):
    wh=w*h
    if h>40 and h<=60:
        return w*40+((h-40)*(w*1.5))
    elif h>60:
        return w*40+((h-41)*(w*1.5))+(h-60)*(w*2.0)
    else:
        return wh

#question 2

def rps(p1, p2):
    rock='R'
    paper="P"
    scissors="S"
    
    if (p1 is rock and p2 is scissors) or (p1 is paper and p2 is rock) or (p1 is scissors and p2 is paper):
        return -1
    elif (p1 is rock and p2 is paper) or (p1 is scissors and p2 is rock) or (p1 is paper and P2 is scissors):
        return 1
    else:
        return 0





















        
    
