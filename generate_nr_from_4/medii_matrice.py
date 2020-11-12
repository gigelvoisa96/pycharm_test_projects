"""Medii aritmetica ale elementelor de pe diagonala, sub diagonala, deasupra diagonalei principale a unei matrice patratice
---------------------"""
if __name__ == '__main__':
    n=int(input('n='))
    a=[]
    for i in range(0,n):
        line=[]
        for j in range(0,n):
            print('a[',i,']=')
            line.append(int(input()))
        a.append(line)
    print("Matrice este:")
    print(a)
    sd,ss,sp=0,0,0
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                sp=sp+a[i][j]
            if i<j:
                sd=sd+a[i][j]
            else:
                ss=ss+a[i][j]
    print('Media de pe diagonala este:', sp / n)
    print('Media sub diagonala este:', ss / ((n**2-n)/2))
    print('Media deasupra diagonalei este:', sd / ((n ** 2 - n) / 2))


