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
def judge_turn_of_four_two(x):
    '''
    >>> judge_turn_of_four_two(1221)
    True
    >>> judge_turn_of_four_two(1234)
    False
    '''
    def rever_number(x):
        pre_y=x
        inve_y=0
        while pre_y > 0:
            inve_y=pre_y%10+inve_y*10
            pre_y=pre_y//10
        return inve_y
    x=int(x)
    pre_x=x
    inve_x= rever_number(x)
    return pre_x==inve_x


            
def my_range_tri(x,y,z):
    '''
    >>> my_range_tri(234,456,213)
    213,234,456,
    '''
    L=[x,y,z]
    L.sort()
    for i in L:
        print(i,end=',')
def money_transformer(n):
    '''
    >>> money_transformer(152)
    152=1*100+1*50+0*20+0*10+0*5+2*1
    '''
    the_number=n
    the_hundred=0
    the_fifty=0
    the_twenty=0
    the_ten=0
    the_five=0
    the_one=0
    the_hundred += n//100
    n=n%100
    the_fifty += n//50
    n=n%50
    the_ten+=n//10
    n=n%10
    the_twenty += n//20
    n=n%20
    the_five += n//5
    n=n%5
    the_one += n
    print("%d=%d*100+%d*50+%d*20+%d*10+%d*5+%d*1" %(the_number,the_hundred,the_fifty,the_twenty,the_ten,the_five,the_one))

