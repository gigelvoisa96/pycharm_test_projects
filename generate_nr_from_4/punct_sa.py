"""
Punct ȘA
Aplicatie: m=3, n=4
A=  2   5   1   -1
    6   7   3   4
    8   1   0   -3
--------------------
Pp ca a_lc si a_pq puncte ȘA

a_lc<=a_lq<=apq

------------------------------
Afisare pozitiilor punctelor sa dintr-o matrice
"""
from numpy import zeros
m=eval(input('m='))
n=eval(input('n='))
a=zeros((m,n), dtype=int)
def Sa(a, m, n,l,c):
    Este_Sa=True
    for j in range(0,n):
        if a[l,j]<a[l,c]:
            Este_Sa = False
    for i in range(0,m):
        if(a[i,c] > a[l,c]):
            Este_Sa = True
    return Este_Sa
print("Dati natura")
for i in range(0,m):
    for j in range(0,n):
        print('a[', i, ']=')
        a[i,j]=eval(input())
print("Natura este", a)
print("Punctele Sa sunt pe pozitiile", end="")
for i in range(0,m):
    for j in range(0,n):
        if Sa(a,m,n,i,j):
            print('{',i, ', ', j, '}', end='')