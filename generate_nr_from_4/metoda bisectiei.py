"""
Metoda bisectiei
------------------
Sa se rezolve(aproximativ) ecuatia cosx=x pe interval[0,pi/2]

//////////////////////////////////////////////////////////////////////////////////////////////////////
Metoda bisectiei (injumatatirii intervalului pentru rezolvarea numericca aproximativa a ecuatiilor"""
from math import cos
from math import pi
def f(x):
    return cos(x)-x

a=float(eval(input('a=')))
b=float(eval(input('b=')))
eps=float(input('eps='))
c=(a+b)/2
while abs(b-a) >=eps:
    if f(c)==0:
        print('radacina este', c)
    elif f(a)*f(c)<0:
        b=c
    else:
        a=c
    c=(a+b)/2
print('radacina aproximativa este ', format(c, '.5f'))
