"""Ordonarea crescatoare a unui sir de numere intregi prin metoda numararii"""
n=eval(input("n="))
a=[]
o=[]
v=[]
for i in range(0,n):
    o.append(0)
    v.append(0)
for i in range(0,n):
    print('a[',i,']=', end='')
    a.append(eval(input()))
print('Sirul dat este: ', a)
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]<=a[j]:
            o[j]=o[j]+1
        else:
            o[i]=o[i]+1
for i in range(0,n):
    v[o[i]]=a[i]
print('Sirul ordonat este: ', v)

