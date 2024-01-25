# Tuples
# elements cannot be added or removed
# the order of elements can not be changed
# works well for representing data structures


x_coordinate = 0
y_coordinate = 0
point:tuple =( x_coordinate,y_coordinate )  # Origin


# Unpack
record:tuple = ('MUTHU',2018,1,19,2598.3, 2000.3,2328.3,2832.5)


class Point:
    __slots__ = ['x','y']
    def __init__(self,x,y) -> None:
        self.x = x 
        self.y = y 
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
    

if __name__=='__main__':

    print(point)

    symbol,year,month,day,*_,close = record
    print(symbol)
    print(year)
    print(month)
    print(day)
    print(*_)
    print(close)
    

    a:tuple = ( Point(0,0), Point(10,10), Point(20,20) )
    print(hex(id(a)))
    print(a)

    # content mutable
    a[0].x = 1000
    print(hex(id(a)))
    print(a)


    # return new tuple if we add
    a += ((10,1))
    print(hex(id(a)))
    print(a)
