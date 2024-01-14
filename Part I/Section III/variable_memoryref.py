
# We can find the memory address that a variable *references*, by using the `id()` function.
# The `id()` function returns the memory address of its argument as a base-10 integer.
# We can use the function `hex()` to convert the base-10 number to base-16.



# [py memory management]('./assets/py_mem_manage.png')



from typing import Any
def memory_check(ele:Any)->None:
    print('ele = {0}'.format(ele))
    print('memory address of ele (decimal): {0}'.format(id(ele)))
    print('memory address of ele (hex): {0}'.format(hex(id(ele))))

if __name__=='__main__':
    number = 10 
    # Strictly speaking, `number` is different from `10` 
    # Instead `number` is a **reference** to an (*int*) object (*containing the value 10*) located at the memory address `id(ele)`
    memory_check(number)