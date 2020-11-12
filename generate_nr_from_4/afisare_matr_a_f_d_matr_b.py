"""afisarea matricii a dupa ordinea data de matricea b"""
from numpy import zeros
m=eval(input('m='))
n=eval(input('n='))
a=zeros((m,n), dtype=int)
b=zeros((m,n), dtype=int)
v=zeros((m*n),dtype=int)
for i in range(0,m):
    for j in range(0,n):
        print('a[',i,j,']=')
        a[i,j]=eval(input())
for i in range(0,m):
    for j in range(0,n):
        print('b[', i, j, ']=')
        b[i,j]=eval(input())
print('a=')
print(a)
print('b=')
print(b)
for i in range(0,m):
    for j in range(0,n):
        v[b[i,j]] = a[i,j]
print("Elementele matricei A dupa ordinea data de B sunt:")
print(v)
