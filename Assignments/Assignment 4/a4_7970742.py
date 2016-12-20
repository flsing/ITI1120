
#open file and read info

def read_initial_info():
    ''' None->(float, 2D-list)
    Reads the file a4-input.txt and returns a tuple. The first element of that tuple is the limit,
    the second is a 2D list called banks of a format as follows (for this particular file a4-input.txt_:
    [[25.0, 1, 100.5, 4, 320.5], [125.0, 2, 40.0, 3, 85.0], [175.0, 0, 125.0, 3, 75.0], [75.0, 0, 125.0], [181.0, 2, 125.0]]

    Before returning the tuple the function should also print the 2D list banks by calling print(banks) 
    '''

    file= open('a4-input.txt','r')
    line= file.read().splitlines()
    limit= float(line[0])


    banks=[]

    for lines in range(1,len(line)):
        banks.append(line[lines].split(' '))
        
   

    for i in range(len(banks)):
        for j in range(len(banks[i])):
            if j %2 != 0:
                (banks[i][j])=int(banks[i][j])
            else:
                (banks[i][j])=float(banks[i][j])

    
    print(banks)

    file.close()
    return limit,banks


    
    
#display the current assets

def current_Assets(banks):
    ''' (2D-list)->list
    given the 2D list banks, returns a (1D) list with the current_assets of all banks
    Precondition: the format of the 2D list banks is as explained in the assignment
    and as produced in read_initial_info()
    '''

    assets=[]
    
    for i in range(len(banks)):
        bsum=0
        for j in range(0,len(banks[i]),2):
               bsum=bsum+banks[i][j]


        assets.append(bsum)

    print(assets)
    return assets
    
                
                
def display_current_assets(assets):
    pair=read_initial_info()
    banks=pair[1]
    
    for i in range(len((banks))):
        
        
        for total in range(int(assets[i]+1)):
            
            total=float(total)
            
            
        print("Bank",i,"Current assets:",total,"millions")
    
        
    
#check the banks if they are safe or not
def check_banks(assets,limit):

    pair=read_initial_info()
    limit=pair[0]
    banks=pair[1]
    assets=current_Assets(banks)
    
    for asset in assets:
        if asset < limit and asset!=0:
            return True
    return False


def current_unsafe(assets):
    pair=read_initial_info()
    limit=pair[0]
    banks=pair[1]
    assets=current_Assets(banks)

    
    for unsafe in range(len(assets)):
    
        
        while assets[unsafe] < limit and not 0:
            
            
            
            return unsafe
        


def current_safe(assets):
    pair=read_initial_info()
    limit=pair[0]
    banks=pair[1]
    assets=current_Assets(banks)

    
    for safe in range(len(assets)):
        
        if assets[safe] >= limit:
            
            print(safe)
            
            
 
            return safe
            
def add_banks():
    for current_unsafe in (assets):
        print("Adding bank",current_unsafe,"to the list of unsafe banks")


        
#FINAL 
def find_unsafe():
    '''None->None

    Your solution goes here. This function should start off by calling read_initial_info()
    and then work with the data read_initial_info() returns, i.e. with limit and 2D list banks
    It should call other helper functions
    '''
    pair=read_initial_info()
    limit=pair[0]
    banks=pair[1]
    assets=current_Assets(banks)
    unsafe=current_unsafe(assets)
    safe=current_safe(assets)
    
    
    
    print("\n\nSafe limit is:", limit,"million dollars\n\n")
    
    
    print("Current unsafe banks are:",unsafe)
    print("Current assets of the banks which are not yet in unsafe list: \n")
    
    display_current_assets(assets)
    
    
    


##    is_banks_unsafe=True
##
##    
##    while is_banks_unsafe:
##
##
##        is_bank_unsafe=check_banks(assets,limit)
##        
##        display_current_assets(assets)
##
##        print("Adding bank",unsafe,"to the list of unsafe banks."
##        current_unsafe_banks
##        
##        is_bank_unsafe=check_banks(assets,limit)

    print("\n\n\nUnsafe banks are:",unsafe)
    print("Safe banks are",safe)

# main
# main can only have this function call and nothing else. Do not modify after this line
find_unsafe()
    
