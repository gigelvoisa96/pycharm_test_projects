"""Cifre maxima a unui numar natural"""
n = eval(input("n="))
m=n
cmax=0
while n!=0:
    c=n%10
    if cmax < c:
        cmax = c
    n=n//10
print('Cifra maxima a numarului: ', m, ' este ', cmax)