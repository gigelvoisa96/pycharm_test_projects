#Generare numar din 4
from numpy import zeros


def generare_numar_din_4(nr):

    m = nr
    v = zeros((20), dtype=int)
    i = 0
    while nr != 4:
        v[i] = nr
        i = i + 1
        if nr % 10 == 0:
            nr=nr//10
        else:
            if nr % 10 == 4:
                nr=nr//10
            else:
                nr=nr*2
            #end_if
        #end_if
    #end_while
    v[i]=4
    print("Secventa de generare a lui ", m," din 4 este:", end=" ")
    for k in range(i, -1, -1):
        print(v[k], end=", ")
    #end_for
#end_def_function


if __name__ == '__main__':
    n = int(input("n="))
    generare_numar_din_4(n)
#end_main