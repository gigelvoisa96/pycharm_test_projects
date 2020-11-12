"""Suma primelor n numere prime"""
from math import sqrt
def Prim(n):
    nrPrim=True
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            nrPrim = False
            break
        return nrPrim
n=eval(input("n="))
s=0
k=1
p=2
while k <= n:
    if Prim(p)==True:
        s=s+p
        k=k+1
    p=p+1
print('Suma primelor ',n,'numere prime este ', s)