import math


class Point:
    'class that represents a point in the plane'

## exectuting Point(2,3)
## 1. creates an object of type point
## 2. calls an objects __init__ method
## 3. produces an object's memory address

## Assigning to a new variable using dot operator
## CREATES THAT VARIABLE INSIDE OF THE OBJECT

## Variables INSIDE of an object are called INSTANCE variables

## __init__ is method that is called to initialize the object (create it and initialize its variables)
## the first parameter of method is usually called self
## self refers to the object that is being initialized


#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'


    
    def distance(self, other):

        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def up(self, dx,dy):

        self.x=self.x
        self.y= self.y + dy

    def down(self,dx,dy):
        self.x=self.x
        self.y=self.y-dy

    def left(self,dx,dy):
        self.x=self.x-dx
        self.y=self.y

    def right(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y
        

class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', age='age'):
        self.spec = species
        self.lang = language
        self.age = age

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def setAge(self, age):

        self.age=age

    def getAge(self):
        return self.age

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec,'and I', self.lang, 'and I am', self.age,'years old.')
    


class Bird(Animal): # class Bird inherits all atributes (data and method) from class Animal 
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print(self.language * 3)



class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit    

    def __repr__(self):
        'return formal representation'
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit


    def __gt__(self,other):

        return self.rank> other.rank and self.suit > other.suit


    def __ge__(self,other):
        
        return self.rank>=other.rank and self.suit >= other.suit

    def __lt__(self,other):
        
        return self.rank < other.rank and self.suit < other.suit


    def __le__(self,other):

        return self.rank <= other.rank and self.suit<= other.suit
        


#excercie 2
class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)


    def __len__(self):
        'returns size of deck'
        return len(self.deck)

    def __repr__(self):
        'returns canonical string representation'
        return 'Deck('+str(self.deck)+')'

    def __eq__(self, other):
        '''returns True if decks have the same cards
           in the same order'''
        return self.deck == other.deck


#excercise 3
class BankAccount:

    def __init__(self, value=0.00):
        self.v=value

    def withdraw(self, dval):
        self.v=self.v-dval

    def deposit(self,dval):
        self.v=self.v+dval


    def balance(self):
        return float(self.v)


    def __repr__(self):
      
        return 'BankAccount('+str(self.v)+')'

##Excersice 4
##class PingPong:
##
##    def __init__(self, ball):
##        self.b=ball
##
##
##    def next(self):
##        return 
##


#excercise 5
class Queue:

    def __init__(self):
        self.q=[]

    def enqueue(self,item):
        self.q.append(item)

    def dequeue(self):
        
        return self.q.pop(0)

    def isEmpty(self):
        return self.q==[]


    def __eq__(self,other):
        return self.q==other.q

    def __repr__(self):

        return 'Queue ('+str(self.q)+')'

    def __len__(self):
        return len(self.q)

        

#excercise 6
class Vector(Point):
    
    def __add__(self,other):
        
        self.newx=(self.x+other.x)
        self.newy=(self.y+other.y)
        
        return 'Vector('+str(self.newx)+','+str(self.newy)+')'


    def __mul__(self,other):
        
        return self.x*other.x + self.y*other.y


    def __repr__(self):

        return 'Vector('+str(self.x)+','+str(self.y)+')'




#excercise 7a
class Marsupial:

    def __init__(self,thing='thing'):
        self.thing=str(thing)
        self.pouch=[]
    
    def put_in_pouch(self,new):
        
        self.pouch.append(new)

    def pouch_contents(self):

        return self.pouch

    def __repr__(self):

        return 'I am a '+(self.thing)+' Marsupial'

        

#excercise 7b        
class Kangaroo(Marsupial):

    def __init__(self,thing='thing',xcoord=0,ycoord=0):
        self.thing=str(thing)
        self.x=xcoord
        self.y=ycoord
        self.pouch=[]

    def jump(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
        
    def __str__(self):

        return 'I am a '+self.thing+ ' Kangaroo located at coordinates ('+str(self.x)+','+str(self.y)+')'



#excercise 8
class Points(Point):

    def __init__(self,lst):
        lst=[]


    def add(self,xcoord, ycoord):
        self.x=xcoord
        self.y=ycoord
        lst.append(self.x,self.y)


    #def left_most_points(self):
        #if i in range(len(lst)):
            


    def __len__(self):
        return len(lst)


    def __repr__(self):
       return 'Points ('+lst+')'
        
        
    
        
