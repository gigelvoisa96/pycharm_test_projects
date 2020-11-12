"""Algoritm medii sir de numere
-------------------------------(Pseudocod)
Read n, an, i=1,n
Spoz:=0
Npoz:=0
Sneg:=0
Nneg:=0
For i=1,n
    If ai < 0 Then
        Sneg:=Sneg + ai
        Nneg = Nneg + 1
    EndIf
    If ai> 0 Theb
        Spoz:= Spoz + ai
        Npoz:=Npoz + 1
    EndIf
EndFor
If Nneg = 0 Then Write 'Nu exista numere negative'
Else Write 'Media aritmetica a numerelor negative este: ', Sneg/Nneg
If Npoz = 0 Then Write 'Nu exista numere pozitive'
Else Write'Media aritmetica a numerelor pozitive este: ', Spoz/ Npoz
"""
from numpy.ma import zeros

""" Mediile aritmetica a unui sir de numere reale"""
n=0
while True:
    n = eval(input('n='))
    if(n!=0): break

a=zeros((n), dtype=int)
Spoz, Npoz, Sneg, Nneg=0, 0, 0, 0

for i in range(0, n):
    print('a[', i, ']=')
    a[i]=float(input())
    if( a[i] < 0):
        Sneg = Sneg + a[i]
        Nneg+=1
    else:
        Spoz = Spoz + a[i]
        Npoz+=1
if(Nneg==0):
    print("Nu exista numere negative")
else:
    print("Media aritmetica a nr negative este: ", Sneg/Nneg)
if(Npoz==0):
    print("Nu exista numere pozitive")
else:
    print("Media aritmetica a nr pozitive este: ", Spoz/Npoz)