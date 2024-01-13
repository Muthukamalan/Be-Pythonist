# 

def division(numerator:int,denominator:int)->None:
    try:
        numerator/denominator
    except ZeroDivisionError as ze:
        print("{}/{} - division by 0".format(numerator,denominator))
    finally:
        print('this always executes!!')
    print('{0}/{1} - main loop'.format(numerator,denominator))
    print('*'*100)
    




def div_with_break_finally(numerator:int,denominator:int)->None:
    # once, break hits, break do only finally block executes
    while numerator<5:
        print('-'*50)
        numerator+=1; denominator-=1
        
        try:
            numerator/denominator
        except ZeroDivisionError as ze:
            print('{0}/{1} - division with zero!!\nBREAK hits!!!'.format(numerator,denominator))
            break                
        finally:
            print('finally always executes!!')

        print('{0}/{1} - main loop'.format(numerator,denominator))
    print('*'*100)



def div_with_continue_finally(numerator:int,denominator:int)->None:
    # once, break hits, continue will run finally block executes and goes to main loop

    while numerator<5:
        print('-'*50)
        numerator+=1; denominator-=1
        
        try:
            numerator/denominator
        except ZeroDivisionError as ze:
            print('{0}/{1} - division with zero\nCONTINUE hits!!!'.format(numerator,denominator))
            continue                
        finally:
            print('finally always executes!!')

        print('{0}/{1} - main loop'.format(numerator,denominator))
    print('*'*100)


if __name__=='__main__':
    division(3,0)
    print()

    div_with_break_finally(0,4)
    div_with_continue_finally(numerator=0,denominator=4)