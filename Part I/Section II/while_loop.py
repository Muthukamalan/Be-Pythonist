# While Loop
# The **while** loop is a way to repeat a block of code as long as a specified condition is met.
# condition evaluates before the loop runs
# we can use `else` with loop


'''py
while (exp is True):
    execute block
else:
    # if WHILE block terminated normally, without encounter BREAK statement
    # if WHILE block not at all executed
'''

def greet_name(min_length:int=2)->str:
    min_length=min_length

    while True:
        name = input("Please enter your name: ")
        if( len(name)>=min_length and name.isprintable() and name.isalpha() ):
            break
    return('Hello, {0}'.format(name))


def print_odd(endl:int=10)->None:
    a = 0 
    while a<endl:
        a+=1
        if a%2==0:
            continue                   # << continue the loop i.e) bye-pass me
        print(a,end='\t')
        print()



def add_if_not_present(list_var:list,value:int )->list:
    length = len(list_var)-1
    while length>=0:
            if list_var[length]==value:
                print('element found!!')
                break
            length-=1
    # Else keyword Usage
    else:
        print('element not in list!!')
        list_var.append(value)
    return(list_var)


if __name__=='__main__':

    i = 5
    # Infinite loop
    while True:

        # >> break << if condition is met
        if(i<10):
            break 
            print("this line never runs!! :(")

        print(i)  
        i+=1

    # Prompt name until name at least name 5 charc long, pprintable and only only alphabets
    greeetings = greet_name(min_length=2)
    print(greeetings)

    # print ODD
    print_odd(10)


    l1:list  = [1,2,3,4,5]
    val1:int = 10 

    print(add_if_not_present(list_var=l1, value=val1))

    l2:list  = [12.4,56.,78.9,5]
    val2:int = 5
    print(add_if_not_present(list_var=l2,value=val2))
    