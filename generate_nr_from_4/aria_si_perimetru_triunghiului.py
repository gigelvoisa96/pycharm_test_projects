"""Se calculeaza aria si perimetrul triunghiului ABC"""
from math import sqrt
from numpy import zeros
"""
def subperimetru(a, b, c):
    lc = sqrt((a[0] - a[1]) ** 2 + (b[0] - b[1]) ** 2)
    lb = sqrt((a[0] - a[1]) ** 2 + (c[0] - c[1]) ** 2)
    la = sqrt((c[0] - c[1]) ** 2 + (b[0] - b[1]) ** 2)
    p = (la + lb + lc) / 2
    return p
"""

def aria(a, b, c, rezult):
    lc = sqrt((a[0] - a[1]) ** 2 + (b[0] - b[1]) ** 2)
    lb = sqrt((a[0] - a[1]) ** 2 + (c[0] - c[1]) ** 2)
    la = sqrt((c[0] - c[1]) ** 2 + (b[0] - b[1]) ** 2)
    p = (la + lb + lc)/2
    print(p)
    rezult[0] = float(p)
    ar = sqrt(p * (p - la) * (p - lb) * (p - lc))
    print(ar)
    rezult[1] = float(ar)

if __name__ == '__main__':
    print("Se introduc punctele:")
    print("A:")
    a=zeros(2, dtype=int)
    b=zeros(2, dtype=int)
    c=zeros(2, dtype=int)
    afis = ["Xa:", "Ya:", "Xb:", "Yb:", "Xc:", "Yc:"]
    for i in range(0,6):
        print(afis[i], end=" ")
        if(i<2): a[i%2] = eval(input())
        if(i<4 and i>=2): b[i%2] = eval(input())
        if(i>=4): c[i%2] = eval(input())
    print("a:", a)
    print("b:", b)
    print("c:", c)
    res = zeros(2, dtype=float)
    aria(a,b,c, res)
    print("res: ",res)
    print("Aria triunghiului este: ", res[1])
    #perimetru = 2*subperimetru(a,b,c)
    print("Perimetrul triunghiului este:", 2*res[0])