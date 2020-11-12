"""Conversia unui numar natural n din baza 10 in baza b, 2<=b<=9
ex. n=38, b=5
38(10)=?(5)
38:5=7, rest=3
7:5=1, rest=2
1:5=0, rest=1
=>numar in baza b(5) este: 123(5)
TEST laborator:
ex de mai sus
Algoritm conversie in baza b
-----------------------------------
Read n, b
i
While n!=0:
    v[i] := n mod b
    i:=i+1
    n:=n div b
EndWhile
For k=i-1, 0
    Write v[i]
EndFor
Stop 
Metoda cu vectori:
-----------------------"""
from numpy.ma import zeros


def method1():

    n = eval(input('n='))
    b = eval(input('b='))
    i = 0
    v = list()
    while n != 0:
        v.append(n % b)
        i += 1
        n //= b
    print("Numarul este: ", end='')
    len = i - 1
    print("Len este:", len)
    print("v este: ", v)
    print("range is:", range(0, len + 1))
    print("Numarul este: ", end='')
    for k in range(0, len + 1):
        val = v[len - k]
        print(val, end='')
    print("\nSfarsit!")


def method2():

    n = int(input('n='))
    b = int(input('b='))
    from math import *
    k = ceil(log10(n) / log10(b)) + 1
    v = zeros((k), dtype=int)
    i = 0
    while n != 0:
        v[i] = n % b
        i = i + 1
        n = n // b
    print('Exprimarea numarului in baza ', b, 'este: ', end='')
    for j in range(i - 1, -1, -1):
        print(v[j], end='')


if __name__ == '__main__':
    method1()
    method2()
