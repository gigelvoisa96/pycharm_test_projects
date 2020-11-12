"""Ordonarea prin metoda bulelor
a = 5,1,0,3,8,2,1,6,4,0     n=10
Medii matrice:
n=3

    [   1   4   6   ]
A=  [   3   2   5   ]
    [   9   9   3   ]
-----------------------------------
Medii Pe diagonala: 2
Medii Sub diagonala:7
Mediii Deasupra diagonalei: 5
-----------------------------------
Citire lista a
"""
if __name__ == '__main__':
    n = eval(input('n='))
    a=list()
    for i in range(0, n):
        print('a[',i,']=', end='')
        a.append(float(input()))
    print("Sirul citit este:")
    print(a)
    ord=False
    while not ord:
        ord=True
        for i in range(0,n-1):
            if(a[i]>a[i+1]):
                a[i],a[i+1]=a[i+1],a[i]
                ord=False
    print("Sirul ordonat este:", end='')
    print(a)