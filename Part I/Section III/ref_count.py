import ctypes
from variable_memoryref import memory_check


def ref_count(address):
    '''tellls how many reference are made by the address you gave'''
    print('number of ref count by {}= {}'.format(hex(address),ctypes.c_long.from_address(address).value))


if __name__=='__main__':
    ele = [1,2,3,4]
    memory_check(ele)
    id_ele = id(ele)
    ref_count(id_ele)

    another_ele = ele
    ref_count(id_ele)

    one_another_ele = ele 
    ref_count(id_ele)

    another_ele = None  # removing one ref 
    ref_count(id_ele) 
