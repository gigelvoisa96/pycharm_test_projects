"""Aria intersectiei dintre n dreptunghiuri din plan"""
""" Test laborator:
n=3
(2,9),(10,4),(4,7),(12,2),(6,8),(9,1)
"""
from numpy import zeros
n = eval(input('n='))
xss = zeros((n), dtype=float)
yss = zeros((n), dtype=float)
xdj = zeros((n), dtype=float)
ydj = zeros((n), dtype=float)
for i in range(0,n):
    print('xss[',i,']=')
    xss[i] = eval(input())
    print('yss[', i, ']=')
    yss[i] = eval(input())
    print('xdj[', i, ']=')
    xdj[i] = eval(input())
    print('ydj[', i, ']=')
    ydj[i] = eval(input())
xstanga = xss[0]
ysus = yss[0]
xdreapta = xdj[0]
yjos = ydj[0]
for i in range(1,n):
    if xstanga<xss[i]:
        xstanga = xss[i]
    if xdreapta > xdj[i]:
        xdreapta=xdj[i]
    if yjos < ydj[i]:
        yjos = ydj[i]
    if ysus > ydj[i]:
        ysus = yss[i]
if((xdreapta < xstanga) or (ysus < yjos)):
    print('intersecite vida')
else:
    A=(xdreapta-xstanga)*(ysus-yjos)
    print("Aria este", A)
