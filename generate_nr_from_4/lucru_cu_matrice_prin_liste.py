"""Inmultirea a 2 matrici
---------------------------
A(m,n), B(n,p), C=AXB, C(m,p)
    [   a11 a12 ... a1n ]
A=  [   a21 a22 ... a2n ]
    [   ... ... ... ... ]
    [   an1 an2 ... ann ]

B=  [   b11 b12 ... b1p ]
    [   b21 b22 ... b2p ]
    [   ... ... ... ... ]
    [   bn1 bn2 ... bnp ]

C=[aij],    i=1,m
            j=1,p
Cij=ai1*b1j+ai2*b2j+...+aik*bkj+...+ain*bnj=suma de la k=1 pana la n de (aik*bkj)
------------------------------------------------------------------------------
------------------------------------------------------------------------------
Algoritm produs de matrici
----------------------------
Read m,n,p,(aij)i=1,m;j=1,n,(bij)i=1,m;j=1,p
For i =1,m
    For j=1,p
        Cij:=0
        For k=1,n
            cij=cij+aik*bkj
        EndFor
    EndFor
EndFor
Write (Cij)i=1,m;j=1,p
Stop
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
Produsul a 2 matrici folosind liste
"""
from numpy import dot
m=eval(input('m='))
n=eval(input('n='))
p=eval(input('p='))
a=[]
b=[]
c=[]
print("Matricea A:")
for i in range(0, m):
    a.append([])
    for j in range(0,n):
        print('a[',i,j,']=')
        a[i].append(float(input()))
print("Dati matricea B:")
for i in range(0, n):
    b.append([])
    for j in range(0,p):
        print('b[',i,j,']=')
        b[i].append(float(input()))
print("A=")
for linie in a:
    print(linie)
print('B=')
for linie in b:
    print(linie)
for i in range(0,n):
    c.append([])
    for j in range(0,p):
        c[i].append(0)
for i in range(0,n):
    for j in range(0,p):
        for k in range(0,n):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]
print('Matricea produs este:')
for linie in c:
    for valoare in linie:
        print(valoare, end=' ')
    print()
print("Rezultatul cu operatorul(functia) dot from numpy este:")
print(dot(a,b))