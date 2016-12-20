import random

def create_board(size):
    '''int->list (of str)
       Precondition: size is even positive integer between 2 and 52    
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    random.shuffle(board)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''(None)->None
    Pauses the program until the user presses enter
    '''
    try:
        input("Press enter to continue ")
    except SyntaxError:
        pass

def play_game(board):
    '''(list of str)->None'''

    create_board(size)


    wait_for_player()
    
    


    
    # The following line of code creates a list indicating what locations are paired, i.e., discovered
    # At the begining none are, so default initializaiton to False is ok
    # You may find this useful
    discovered=[False]*len(board) 

   # YOUR CODE GOES HERE
   # this is the funciton that plays the game





# MAIN 

print("How many cards do you want to play with?")
size=int(input("Enter an even number between 2 and 52: "))


# this creates the board for you of the given size
board=create_board(size)

# this calls your play_game function that plays the game
play_game(board)
