"""Calcul aproximativ al lui radical(a)
-----------------------------------------
Se stie ca sirul este recurent
x_n=1/2(x_n-1 + a/(x_n-1)) | lim(n->infinit)
este convergent si lim"x->infinit" de (x_n) = radical(a)
l=1/2(l+a/l)
2*l**2=l**2+a
l**2=a
l=radical(a)
a=x0,x1,x2,..., xk, ...
==========================================
Algoritm radical din a
------------------------------
Read a, eps
x=a
y=1/2(x+a/x)
while | y - x | >= eps
    x:=y
    y:=1/2(x+a/x)
write y
============================================
Calcul aproximativ radical din a
--------------------------------------------
"""
from math import sqrt
def radical(a,eps):
    x=a
    y=1/2*(x+a/x)
    while abs(x-y) >=eps:
        x=y
        y=1/2*(x+a/x)
    return y
if __name__ == '__main__':
    while True:
        a=eval(input('a='))
        if a > 0: break
    eps=eval(input('eps='))
    print("Radical aproximativ = ", radical(a,eps))
    print("Radical cu sqrt = ", sqrt(a))