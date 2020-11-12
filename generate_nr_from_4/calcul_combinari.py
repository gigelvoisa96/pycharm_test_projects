#Calcul combinarilor


def calcul_combinari(m, n):
    c=1
    for i in range(1, n+1):
        c=c*(m-i+1)/i
    print("combinari de ", m, " luate cate ", n, " = ", int(c))


if __name__ == '__main__':
    m=int(input("m="))
    n=int(input("n="))
    calcul_combinari(m,n)