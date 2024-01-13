# Custom Classes

# To create a class we use `class` keyword and we can initialize class attributes in the special method `__init__`

# values that belongs to class -> `properties`
# functions  that belongs to class -> `methods`



from typing import Union
class Rectangle:
    '''
        class Rectangle docstring
    '''
    def __init__(self,width:Union[int,float],height:Union[int,float]) -> None:
        ''' width & height are property of Rectangle class '''
        self.width:int   = width
        self.height:int  = height

    def area(self)->int:
        '''area=width*height'''
        return self.width*self.height
    
    def perimeter(self)->int:
        '''perimeter= 2*(width+height)'''
        return 2*(self.width+self.height)

    def __str__(self) -> str:
        return('Rectangle with {0:.3f} width and {1:.2f} height'.format(self.width,self.height))
    
    def __eq__(self, __value) -> bool:
        ''' compare both rectangle'''
        print('self={0},other={1}'.format(self,__value))
        if isinstance(__value,Rectangle):
            return self.width==__value.width and self.height==__value.height
        return False
    
    def __lt__(self, __value: object) -> bool:
        '''less than current rectangle  r1<r2'''
        if isinstance(__value,Rectangle):
            return self.area()<__value.area()
        return NotImplemented



# Applying getter and setter property of class
class Square:
    def __init__(self,side:int) -> None:
        self._a = side
    
    # property
    @property
    def a(self):
        '''getting side of a square'''
        return self._a
    

    # @property.setter
    @a.setter
    def a(self,new_value):
        ''' setting new value to side of a square'''
        if isinstance(new_value,int) and new_value>=0:
            self._a = new_value
        else:
            raise ValueError('side should be Positive value!!')


    def __eq__(self, __value: object) -> bool:
        if isinstance(__value,Square):
            return self.a ==__value.a
        return False

    def __str__(self) -> str:
        return('Square of side={}'.format(self.a))
        

if __name__=='__main__':
    r1 = Rectangle(10,20)
    print(r1.area())
    print(r1.perimeter())

    print(r1)
    print(r1.__repr__())   # << In jupyter (and interactive console if you're using that)

    r2 = Rectangle(10,20)
    r3 = Rectangle(1,2)
    print(r2==r3)          # << r2 .__eq__(r3)

    print(r2 is r3)
    print(r3 < r2)

    s1 = Square(10)
    print(s1)
    try:
        s1.a = -34
    except Exception as e:
        print(e.__repr__())
    finally:
        print(s1)
