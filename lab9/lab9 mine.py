def min_or_max_index(L,boo):

    
    if boo == True:
        for i in range(len(L)):
            for j in range(i+1,len(L)):
                if L[i] <= L[j]:
                    L[i]=L[j]
        return i,[i]
                
            
        return (i,[i])
    if boo== False:
        for i in range(len(L)):
            if L[i]>i+1:
                return (i,[i])
                       
