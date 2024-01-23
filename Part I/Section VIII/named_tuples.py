from tuples_as_datastruct import Point
from collections import namedtuple   
# namedtuple is a function which generate a new class, that new class inherits from tuple it comes with named properties
# class factory


Point2D = namedtuple('Point2D',['x','y'])

pt = Point2D(10,20)






if __name__=='__main__':
    print(pt)