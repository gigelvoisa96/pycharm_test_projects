"""Calcul suma inverselor cu recursivitate"""
def suma_rec(k):
    s=0
    if k==1:
        return 1
    else:
        s=1./k+suma_rec(k-1)
        return s
n=int(input('n='))
print('suma inverselor primelor ', n, ' numere naturale este: ', format(suma_rec(n),'.6f'))
