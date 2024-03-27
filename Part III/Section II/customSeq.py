# Understand `__getitem__` works

colors:list = ['crimson','ruby','brick','scarlet','maroon','raspberry','coral','redwood']
print(colors.__getitem__(5))

try:
    colors.__getitem__(100)
except IndexError as ie:
    # raise IndexError
    print(ie.__class__)


print(colors.__getitem__(slice(2,4)))
print(colors.__getitem__(slice(None,None,-1)))



class MySequece:
    def __getitem__(self,idx):
        print(type(idx),idx)

s = MySequece()
s[100]
s['test']
s[:10:2]



class MyClass:
    def __init__(self,name) -> None:
        self.name = name
    def __repr__(self) -> str:
        return f"MyClass(name={self.name})"
    
    def __add__(self,other):
        return MyClass(self.name + ' '+ other.name)
    def __iadd__(self,other):
        self.name+= ' ' + other.name
        return self.name
    
    def __mul__(self,n):
        return MyClass(self.name * n)
    def __imul__(self,n):
        self.name *= n 
        return self.name
    
    # repeation
    def __rmul__(self,n):
        self.name *= n 
        return self.name
    
    def __contains__(self,value):
        return value in self.name
    

x:MyClass = MyClass("hello")
y:MyClass = MyClass("world")
z:MyClass = MyClass("programming")

print(x+y)
x+=z
print(x)
print(y*2)
y*=3
print(y)
print('h' in x)


import numbers
class Point:
    ''' #Point '''
    def __init__(self,x,y) -> None:
        if isinstance(x,numbers.Real) and isinstance(y,numbers.Real):
            self.pt = (x,y)
        else:
            raise TypeError("Point co-ordinates must be real no.")
        
    def __repr__(self) -> str:
        return f"Point(x={self.pt[0]}, y={self.pt[1]})"
    
    def __len__(self):
        return 2
    def __getitem__(self,idx):
        return self.pt[idx]
    

class Polygon:
    ''' #Polygon '''
    def __init__(self,*pts) -> None:
        if pts:
            self._pts =[ Point(*pt) for pt in pts]
        else:
            self._pts=[]

    def __len__(self):
        return len(self._pts)
    
    def __getitem__(self,idx):
        return self._pts[idx]

    def __repr__(self) -> str:
        return "Polygon({})".format(self._pts)
    
    def __add__(self,other):
        if isinstance(other,Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError("can only concat with another polygon")
        
    def __iadd__(self,other):
        if isinstance(other,Polygon):
            self._pts += other._pts
        else:
            # raise TypeError("can only concat with another Polygon")
            points = [Point(*pt) for pt in other]
            self._pts += points
        return self

    def insert(self,idx,pt):
        self._pts.insert(idx,Point(*pt))

    def __delitem__(self,s):
        del self._pts[s]


p = Point(1,2)
print(hex(id(p)), p)


p1 = Polygon(*zip(range(6), range(6)))

del p1[1]
p2 = Polygon((0,0), (1,1))

p1+=p2
print(hex(id(p1)), p1)