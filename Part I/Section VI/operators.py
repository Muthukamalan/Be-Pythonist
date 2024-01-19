import operator


my_list = [1, 2, 3, 4]

class MyClass:
    __slots__= 'a','b','c'
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        
    def test(self):
        print('test method running...')
    
    def do_something(self, c):
        return(self.a, self.b, c)

has_a_attribute = operator.attrgetter('a')
has_a_c_attribute = operator.attrgetter('a','c')
has_f_attribute = operator.attrgetter('f')
f = operator.attrgetter('test')

if __name__=='__main__':
    print(dir(operator))
    print(operator.and_(True, False))
    operator.setitem(my_list, 1, 100)
    print(my_list)
    operator.delitem(my_list, 3)
    print(my_list)

    x = MyClass()
    print(has_a_attribute(x))
    print(has_a_c_attribute(x))
    try:
        print(has_f_attribute(x))
    except AttributeError as ae:
        print(ae.__repr__())

    print('do something',operator.attrgetter('do_something')(x)(20))
    print('do something',operator.methodcaller('do_something',c=200)(x))
