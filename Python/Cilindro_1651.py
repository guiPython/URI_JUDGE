from math import pi

def Circ_Base(l1,l2):
    if (l1>=l2): return pi * (l2/2)**2 *l2/2, 2 * pi * l2/2
    else: return pi * (l1/2)**2 *l1/2, 2 * pi * l1/2

A , Comp_C = Circ_Base(10,30)
print(A,Comp_C)

def Circ_Corpo(Comp_C,l1,l2):
    if (l1>=l2) :
        return (Comp_C - l2)/2
    else: return(Comp_C - l1)/2

print(Circ_Corpo(Comp_C,10,30))