"""Ordonarea punctelor din plan dupa ordonarea descrescatoare a distantelor la origine
---------------------------------------------------------------------------------------"""
from numpy import zeros
from math import sqrt

if __name__ == '__main__':
    n=int(input('n='))
    x=zeros((n), dtype=int)
    y=zeros((n), dtype=int)
    d = zeros((n), dtype=float)
    for i in range(0,n):
        print('x[',i,']=',end='')
        x[i]=int(input())
        print('y[',i,']=',end='')
        y[i]=int(input())
        d[i]=sqrt(x[i]*x[i]+y[i]*y[i])
    ordonat=False
    while not ordonat:
        ordonat=True
        for i in range(0, n-1):
            if d[i]<d[i+1]:
                d[i],d[i+1]=d[i+1],d[i]
                x[i],y[i],x[i+1],y[i+1]=x[i+1],y[i+1],x[i],y[i]
                ordonat=False
    print("Punctele ordonate sunt:", end='')
    for i in range(0,n):
        print('(',x[i],', ',y[i],')', end='')
