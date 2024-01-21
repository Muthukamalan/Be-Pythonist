# global scope refers to the module scope

a:int = 10   # << define in module, so it's global scope 


# its accessible in any innner
# Remember: Functions defined inside another function can access the outer (nonlocal) variables
def foo(n:int)->int:
    print('accessible global var inside function, global::{0}'.format(a))
    return( a**n )


# disclaimer
def change_global_var(val:int)->None:
    a = val
    print("value changed!!")


# declaring global vaiable inside function
def declare_global_inside_func(n:int)->None:
    global y 
    y = n 


a:int = 1
b:int = 2
def UnboundLocalCondiition():
    print(f"a={a}, b={b}")
    b=3                              #  change b->e, works fine, WHY?
# a,b are global scope, but they're reference before assign value in the local scoppe.


# NONLocal Scopes
# Functions defines inside the another function can reference variables from enlosed scope, similarly to function can look for global scope

def outer_function()->None:
    x = 'I\'m outer function variable!!'
    def inner_function()->None:
        print('executing from inner function, ',end='\t')
        print(x) 
    inner_function()



# Nested Scope
    
def call_grandpa()->None:
    grandpa_name:str = 'paul!!'
    def pa()->None:
        pa_name:str = 'mariappan'
        def me()->None:
            name:str = 'muthu'
            def son()->None:
                print(f"son calling...",name,pa_name,grandpa_name)
            son()
        me()
    pa()



# if we use same variable, considered part of the local scope
def before_17th()->None:
    x:str = 'earth is flat'
    def modern_age()->None:
        x:str = 'earth is spherical'
    modern_age()
    print(x)



# if you ANNOTATE below code will throw error
def people_at_90()->None:
    x = 'work harder'
    def people_at_2k()->None:
        nonlocal x                          # nonlocal make x as from outer reference
        x = 'work smarter'
    people_at_2k()
    print(f'current mindset ::',x)




'''
# Compile Time Error itself.
x = 100
def outer():
    global x
    x = 'python'
    
    def inner():
        nonlocal x;
        x = 'monty'
    inner()

    
# But this will not work. In `inner` Python is looking for a local variable called `x`. `outer` has a label called `x`, but it is a global variable, not a local one - hence Python does not find a local variable in the scope chain.
'''



def adulthood():
    age = '67'
    def teenage():
        age = '20'
        def childhood():
            nonlocal age
            age = '6'
        print('teenage):', age)
        childhood()
        print('(after) called childhood :', age)
    teenage()
    print('adulthood:', age)

if __name__=='__main__':
    print(f"global decalre:: a={a}")
    
    # accessible inside function
    foo(1)

    # able to change global var
    change_global_var(20)

    # declare global variable
    declare_global_inside_func(30)
    try:
        print(f"is globally declare y::{y}")
    except NameError as e:
        print(e.__repr__())


    try:
        UnboundLocalCondiition()
    except Exception as ule:
        print(ule.__repr__())


    outer_function()
    call_grandpa()
    before_17th()
    people_at_90()

    adulthood()