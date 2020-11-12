"""Afisarea numarului in oglinda"""
n = eval(input("n="))
while n != 0:
    print(n % 10, end='')
    n = n // 10
