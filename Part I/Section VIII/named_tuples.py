from collections import namedtuple   
# namedtuple is a function which generate a new class, that new class inherits from tuple it comes with named properties
# class factory
# Immutable


point3D = namedtuple('Point3D','x y z')

Point2D = namedtuple('Point2D',['x','y'])
pt1 = Point2D(x=10,y=20)
pt_2 = Point2D(x=10,y=20)


from tuples_as_datastruct import Point
pt2 = Point(x=100,y=200)


# Extending a Named Tuple
point_4_fields = point3D._fields + ('gamma',)
point4D = namedtuple('Point4D',point_4_fields)
pt4 = point4D(1,2,3,4)

if __name__=='__main__':
    print(Point2D.__doc__)
    print(pt1)
    print(isinstance(pt1,tuple))
    print(type(pt1))
    print(pt1._asdict())
    print(f"__eq__",pt1==pt_2)
    print(f"__is__",pt1 is pt2)
    
    print(pt2)
    print(isinstance(pt2,tuple))
    print(type(pt2))

    pt3  = point3D(50,60,70)
    print('max in 3d point',max(pt3))
    print('slice it 🔪',pt3[0:2])
    print(pt3._fields)

    try:
        pt3.x = 100
    except AttributeError as ae:
        print(ae.__repr__())

    old_x,*old_other_values =pt3
    pt3 = point3D(10,*old_other_values)
    print(pt3)


    pt4 = pt4._replace(gamma=1000)
    print(pt4)
    

    point4D.__doc__= '4D cartisian co-ordinate'
    point4D.x  = 'gamma in 4D'
    print(point4D.__doc__)
    print(point4D.x.__doc__)

    # default Values
    print('defaults:',pt4.__new__.__defaults__)
    pt4.__new__.__defaults__ = (90,100)  # setting z=90 and gamma=100
    pt4 = point4D(23,34)
    print(pt4)