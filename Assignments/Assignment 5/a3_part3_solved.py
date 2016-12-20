class Point:
    'class that represents a point in the plane'

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
        '''(Point,Point)->bool
        self == other if they have the same coordinates'''
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


class Rectangle:
    def __init__(self, bp, tp, color):
        '''(Rectangle, Point, Point, str)->None'''
        self.bp=bp
        self.tp=tp
        self.color=color
        
    def get_bottom_left(self):
        '''(Rectangle)->Point'''
        return self.bp
    
    def get_top_right(self):
        '''(Rectangle)->Point'''
        return self.tp
    
    def get_color(self):
        '''(Rectangle)->str'''
        return self.color
    
    def reset_color(self,newcolor):
        '''(Rectangle,str)->None'''
        self.color=newcolor

    def get_perimeter(self):
        '''(Rectangle)->number'''
        return 2*(self.tp.x-self.bp.x) + 2*(self.tp.y-self.bp.y)

    def get_area(self):
        '''(Rectangle)->number'''
        return (self.tp.x-self.bp.x)*(self.tp.y-self.bp.y)

    def move(self, dx,dy):
        '''(Rectangle,number,number)->None'''
        self.bp.move(dx,dy)
        self.tp.move(dx,dy)

    def intersects(self,other):
        '''(Rectangle,Rectangle)->bool'''
        # if self to the right of other or other to the right of self, return False
        if self.tp.x < other.bp.x or other.tp.x < self.bp.x:
            return False
        # or if self below other or other below self
        elif self.tp.y < other.bp.y or other.tp.y < self.bp.y:
            return False
        else:
            return True

    def contains(self,x,y):
        '''(Rectangle,number,number)->bool'''
        return (self.bp.x  <= x) and (x <= self.tp.x) and (self.bp.y <= y) and (y <= self.tp.y) 
        

    def __eq__(self,other):
        '''(Rectangle,Rectangle)->bool'''
        return self.bp==other.bp and self.tp==other.tp and self.color==other.color

    def __repr__(self):
        '''(Rectangle)->str'''
        return 'Rectangle('+str(self.bp)+","+str(self.tp)+","+'\''+self.color+'\')'


    def __str__(self):
        '''(Rectangle)->str'''
        return 'I am a '+self.color+' rectangle with bottom left corner at '+str(self.bp.get())+' and \
top right corner at '+str(self.tp.get())+'.'

class Canvas:
    def __init__(self):
        '''(Canvas)->None'''
        self.q=[]

    def add_one_rectangle(self,other):
        '''(Canvas, Rectangle)->None'''
        self.q.append(other)

    def count_same_color(self, color):
        '''(Canvas, str)->int'''
        count=0
        for item in self.q:
            if item.color==color:
                count=count+1
        return count

    def total_perimeter(self):
        '''(Canvas)->number'''
        total=0
        for item in self.q:
            total=total+item.get_perimeter()
        return total

    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle'''
        minx=[]
        maxx=[]
        miny=[]
        maxy=[]

        for item in self.q:
            minx.append(item.bp.x)
            maxx.append(item.tp.x)
            miny.append(item.bp.y)
            maxy.append(item.tp.y)

        return Rectangle(Point(min(minx), min(miny)), Point(max(maxx), max(maxy)), "red")

    def common_point(self):
        '''(Canvas)->bool'''
        for i in range(len(self.q)):
            for j in range(i+1, len(self.q)):
                if not( self.q[i].intersects(self.q[j]) ):
                    return False
        return True
        
    def __len__(self):
        '''(Canvas)->int'''
        return len(self.q)

    def __repr__(self):
        '''(Canvas)->str'''
        return 'Canvas('+str(self.q)+')'
