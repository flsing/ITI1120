def read_initial_info():
    ''' None->(float, 2D-list)
    Reads the file a4-input.txt and returns a tuple. The first element of that tuple is the limit,
    the second is a 2D list called banks of a format as follows (for this particular file a4-input.txt_:
    [[25.0, 1, 100.5, 4, 320.5], [125.0, 2, 40.0, 3, 85.0], [175.0, 0, 125.0, 3, 75.0], [75.0, 0, 125.0], [181.0, 2, 125.0]]

    Before returning the tuple the function should also print the 2D list banks by calling print(banks) 
    '''
    lines = open('a4-input-3.txt').read().splitlines()
    limit=float(lines[0])
    banks=[]
    for i in range(1,len(lines)):
        bank=[]
        line=lines[i].split()
        for i in range(len(line)):
            if i%2==0:
                bank.append(float(line[i]))
            else:
                bank.append(int(line[i]))
        banks.append(bank)
    print(banks)
    print()
    return (limit,banks)

def print_status(unsafe_banks, current_assets):
    ''' (list, list)->None'''
    print("Current unsafe banks are:", end= " ")
    for bank in unsafe_banks:
        print(bank, end=" ")
    print()
    print("Current assets of the banks which are not yet in unsafe list:")
    for b in range(len(current_assets)):
        if b not in unsafe_banks:
            print("Bank", b, "Current assets:", current_assets[b], "millions")
    print("\n")

def print_final(unsafe_banks, banks):
    unsafe_banks.sort()
    print("Unsafe banks are: ", end=" ")
    for bank in unsafe_banks:
        print(bank, end=" ")
    print()
    print("Safe banks are: ", end=" ")
    for i in range(len(banks)):
        if i not in unsafe_banks:
            print(i, end=" ")

def current_Assets(banks):
    ''' (2D-list)->list
    given the 2D list banks, given in the format as produced in read_initial_info()
    returns a 1D list with the current_assets of all banks
    '''
    
    current_assets=[]
    for i in range(len(banks)):
        asset=0
        for j in range(0,len(banks[i]),2):
            asset=asset+banks[i][j]
        current_assets.append(asset)
    return current_assets

def find_unsafe():
    '''None->None

    Your solution goes here. This function should start off by calling read_initial_info()
    and then work with the data read_initial_info() returns.
    It should call other helper functions
    '''
    pair=read_initial_info()
    limit=pair[0]
    print("Safe limit is:", limit,"million dollars\n\n")
    banks=pair[1]

    unsafe_banks=[]
    new_unsafe=True
    while new_unsafe:
        current_assets=current_Assets(banks)
        print_status(unsafe_banks, current_assets)
        new_unsafe=False
        #find one unsafe, if it exists
        for i in range(len(current_assets)):
            if i not in unsafe_banks and current_assets[i]<limit:
                new_unsafe=True
                new_unsafe_bank=i
                unsafe_banks.append(i)
                print("Adding bank", i, "to the list of unsafe banks.")
                break
        # update info of currently safe banks if new unsafe found
        if(new_unsafe): 
            for j in range(len(banks)):
                if j not in unsafe_banks:
                    for k in range(1,len(banks[j]),2):
                        if banks[j][k]==new_unsafe_bank:
                            banks[j][k+1]=0
    print_final(unsafe_banks,banks)

# main
# main can only have this function call and nothing else
find_unsafe()
    
