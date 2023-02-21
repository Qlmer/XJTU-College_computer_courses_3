import math
def arch_to_m_square(n):
    '''
    >>> arch_to_m_square(10)
    6666.6670
    '''
    k=float(n)
    result=k*(666.6667)
    print("%-10.4f"% result)
def complex_add_and_sub(x,y):
    '''
    >>> complex_add_and_sub(1+1j,1-1j)
    ((2+0j), 2j)
    '''
    return x+y,x-y
def input_complex(x,y):
    '''
    >>> input_complex(1,2)
    (1+2j)
    '''
    return complex(x,y)

def judge_tri(x,y,z):
    '''
    >>> judge_tri(4,5,6)
    True
    '''
    L=[x,y,z]
    L.sort()
    if L[0] + L[1] > L[2]:
        return True
    else:
        return False


def judge_turn_of_four(x):
    '''
    >>> judge_turn_of_four(1221)
    True
    >>> judge_turn_of_four(1234)
    False
    '''
    k=int(x)
    S_1=str(k)
    S_2=S_1[::-1]
    if S_2 == S_1:
        return True
    else:
        return False
def my_range_tri(x,y,z):
    '''
    >>> my_range_tri(234,456,213)
    213,234,456
    '''
    L=[x,y,z]
    L.sort()
    for i in L:
        print(i,end=',')

