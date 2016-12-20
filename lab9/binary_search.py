def binary_search(L,v):
     '''
     (list,object)->bool

     Returns an index of v in L
     or returns -1, if v not in L
     
     Precondition: L is sorted
     '''
     b = 0
     e = len(L)- 1

     while e >= b:
          mid = (b + e) // 2
          if (key < L[mid]):
               e = mid - 1
          elif (key == L[mid]):
               return mid
          else:
               b = mid + 1
               
     return - 1; # Now high < low


def first_one(L):

     b=0
     e = len(L) - 1

     while b != e + 1:
          mid = (b + e) // 2
          if L[mid] < 1:
               b=mid+1

          elif L[mid]==1:
               return b
          else:
               e=mid-1

     
          
     if 1 <= b < len(L) and L[b] == 1:
          return b
     else:
          return -1

#def last_zero(L):

     
     b=0
     e = len(L) - 1

     while b != e + 1:
          mid = (b + e) // 2
          if L[mid] > 0:
               b=mid+1

          else:
               e=mid-1

     
          
     if 0 <=e < len(L) and L[b] == 0:
          return b
     else:
          return -1




     
