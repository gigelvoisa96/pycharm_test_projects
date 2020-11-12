"""Schema lui Horner"""
"""Test laborator:
S. Horner:
n=5
P(n)=2n**5-3n**4+4*n+7
:(x-2)
CAtul:2x**4+x**3+2x**2+4x+12
Restul: 31"""
from numpy import zeros
n = eval(input('n='))
a = zeros((n+1), dtype=int)
b = zeros((n+1), dtype=int)
for i in range(0,n+1):
    print('a[', i, ']=')
    a[i] = eval(input())
c=int(input('c='))
b[0]=a[0]
for i in range(1,n+1):
    b[i] = c*b[i-1]+a[i]
print("Coeficientii catului sunt: ", end='')
for i in range(0,n):
    print(b[i], end='')
print("Restul este: ", b[n])