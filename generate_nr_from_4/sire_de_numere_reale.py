"""
Se da sirul de numere reale a1, a2, ..., an
Sa se inlocuiasca fiecare termen al sirului cu media aritmetica a celorlalti termeni din sir
Figura generala
----------------------------
| a1 | a2 | a3 | ... | an |
----------------------------

Fiecare termen din sir este media aritmetica a celorlalti termeni din stanga?
Algoritm inlocuire termeni sir
-------------------------------
Read n, a[i], i=1,n
s:=0
For i:=1,n
    S=S+ai
EndFor
For i:=1, n
    ai:=(S-ai)/(n-1)
EndFor
write a
stop
--------------------------------
Inlocuire termeni sir
"""
from numpy import zeros
print("n=", end=" ")
n=eval(input())
a=zeros((n+1), dtype=float)
for i in range(1,n+1):
    print('a[',  i, ']=')
    a[i]=int(input())
S=0
for i in range(1, n+1):
    S=S + a[i]
for i in range(1, n+1):
    a[i]=(S-a[i])/(n-1)
print(a)
