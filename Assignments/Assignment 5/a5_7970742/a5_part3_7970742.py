class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord


    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

    
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In the case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle(Point):
    'class that represents a Rectangle on the plane'

    def __init__(self, Point1, Point2, color):
        '''(Rectangle,Point, Point, str) -> None
        initialize rectangle coordinates to (point, point) and sets color'''
        self.col=str(color)
        
    
        
        self.left=Point1
        

        
        self.right=Point2
        
        
     


    def get_bottom_left(self):
        '''(Rectangle)->tuple
        Returns a tuple with x and y coordinates of the bottom left point of
        the rectangle'''
        
        return self.left


    def get_top_right(self):
        '''(Rectangle)->tuple
        Returns a tuple with x and y coordinates of the top right point of
        the rectangle'''

        return self.right

    def get_color(self):
        '''(Rectangle)->str'''

        return self.col


    def reset_color(self,color):
        '''(Rectangle, str)->None'''

        self.col=color


    def get_perimeter(self):
        '''(Rectangle)->int'''
        

        
        return 2*(self.right.x-self.left.x)+2*(self.right.y-self.left.y)



    def get_area(self):
        '''(Rectangle)->float
        Return the area of the rectangle by multiplying the width times lengh'''

        return (self.right.x-self.left.x)*(self.right.y-self.left.y)


    def move(self,dx,dy):
        '''(Rectangle,number,number)->None
        changes the x and y coordinates by dx and dy'''
        
        
        self.left.x += dx
        self.right.x +=dx
        self.left.y+=dy
        self.right.y += dy
        
                

    def intersects(self,other):
        '''(Rectangle, Rectangle)->bool
        Returns True if self and other have a point in common.
        If not it return False'''

       # if 
##
##        
##        if other.x <= self.right.x and other.x >= self.left.x and othery==self.left.y or othery--self.right.y:
##            return True
##        else:
##            return False
        

    def contains(self, otherx,othery):
        '''(Rectangle, number, number)->bool
        Returns True if the Point with x and y coord are inside the rectangle.
        If not false '''

        
        if otherx<=self.right.x and otherx >= self.left.x and othery <=self.right.y and othery >= self.left.y:
            return True
        else:
            return False



    def __eq__(self,other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other have the same coordinates'''

        return self.right == other.right and self.left == other.left

    def __repr__(self):
        '''(Rectangle)->str
        Returns a canonical representation Rectangle(Point, Point, color).'''
       
        return 'Rectangle('+str(self.left)+','+str(self.right)+', '+str(self.col)+')'

    def __str__(self):
        '''(Rectangle)->str
        Returns a nice string representation of Rectangle(Point, Point).
        With its color and bottom left corner, and top right corner'''
       
        return 'I am a '+ str(self.col)+' rectangle with bottom left corner at '+str(self.left)+' and top right corner at '+str(self.right)+'.'
    

class Canvas(Rectangle):
    
    def __init__(self):
        '''(Canvas)->None'''

        self.canvas=[]
        
        




    def add_one_rectangle(self,rectangle):
        '''(Canvas,rectangle)->lst'''
        
        self.canvas.append(rectangle)
        
        



    def count_same_color(self,color):
        '''(Canvas,str)->int'''

        
        i=0
        for color in self.canvas:
            i=i+1
        return i
        



    def total_perimeter(self):
        '''(Canvas)->int'''
        
        super().get_perimeter()




    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle'''
        super().__init__(Point1, Point2, color)
        return 'Rectangle(Point'+str(min(self.left.x))+','+str(min(self.left.y))+'Point('+str(max(self.right.x))+','+str(max(self.right.y))+','+str(color)+')'


##
##    def common_point(self):
##        '''(Canvas)->bool'''
##
##
##
##

    def __len__(self):
        '''(Canvas)->int'''
        
        return len(self.canvas)




    def __repr__(self):
        '''(Canvas)->str'''
        
        return "Canvas("+str(self.canvas)+")"



