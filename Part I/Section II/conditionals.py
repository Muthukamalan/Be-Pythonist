# A conditionals is a construct that allows you to branch your code on based conditions being met


# Ternary operator
# variable =  'True' if (condition) else 'False'

a = 2

if __name__=='__main__':
    
    if (a<3): print('a < 3')
    else: print('a >=3')

    if (a<0): print('a < 0')
    elif(a<10): print('a < 10')
    else:
        print('a > 10')
    
    res = 'a < 10' if a< 10 else 'a>10'
    print(res)