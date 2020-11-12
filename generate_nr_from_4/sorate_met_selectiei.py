"""Ordonarea crescatoare a unui sir de numere intregi prin metoda selectiei"""
n=eval(input("n="))
a=[]
for i in range(0,n):
    print('a[',i,']=',end='')
    a.append(eval(input()))
print("Sirul dat este: ", a)
for i in range(0,n):
    min=a[i]
    indice_min=i
    for j in range(i+1, n):
        if a[j]<min:
            min=a[j]
            indice_min=j
    a[indice_min]=a[i]
    a[i]=min
print('Sirul ordonat este: ', a)