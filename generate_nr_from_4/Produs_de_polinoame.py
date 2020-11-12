"""Produs de polinooame
----------------------------
Algoritm produs de polinoame
------------------------------
Read n,m,(ai)i=1,n,(bj)j=0,m
For k=0,m+n
    ck:=0
For i=0,n:
    For j=0,m:
        c[i+j]=c[i+j]+a[i]*b[j]
    EndFor
EndFor
Write(C[k],k=0,m+n
-------------------------------
Produs de plinoame
-------------------------------
"""
m=eval(input('m='))
n=eval(input('n='))
P=[]
Q=[]
R=[]
for i in range(0, m+1):
    print('P[',i,']=')
    P.append(int(input()))
for j in range(0, n+1):
    print('Q[',i,']=')
    Q.append(int(input()))
for k in range(0, m+n+1):
    R.append(0)
for i in range(0, m+1):
    for j in range(0, n+1):
        R[i+j]=R[i+j]+P[i]*Q[j]
print("polinomul P este", P)
print("polinomul Q este", Q)
print("polinomul R este", R)
