# An object whose internal state can be changed, is call *mutable*
# An object whose internal state can not be changed, is call *immutable*


# IMMUTABLE 
#   - numbers(int,float,bool,complex,etc.)
#   - str
#   - tuples
#   - frozen set

# MUTABLE
#   - list
#   - set
#   - dict



class Rectangle:
    def __init__(self,width, height ) -> None:
        self.width = width 
        self.height = height

    def area(self):
        return self.width*self.height
    
    def __str__(self) -> str:
        return( f"Rectangle:: self={hex(id(self))}; width={hex(id(self.width))}; height={hex(id(self.height))}; area={hex(id(self.area))}" )
    

if __name__=='__main__':
    r1 = Rectangle(width=1,height=3)
    print(r1)

    # Internal state of Obj and Memory Changed!!
    r1.width = 12 
    print(r1)

    t1 = (1,2,3,[4,5])  # Immutable but access index of tuple was mutable
    print(t1)
    t1[-1][0]=30        # changed list state
    print(t1) 
