"""Calculare distanta intr-un timp dat"""


def merge_un_minut(distanta_actuala, dx):
    return distanta_actuala + dx


def oboseste_magarusul(dx):
    print("Magarusul a obosit!")
    return dx/2


def trece_un_minut(distanta_actuala):
    print("Magarusul a facut ", distanta_actuala, " metri!")


def fa_calcule(dx, n, finish):
    print("metri pe un minut: ", dx)
    print("dupa cate minute o sa oboseasca magarusul? R: ", n)
    print("pana cati metri o sa ma tot duc? R: ", finish)
    if finish<1:
        print("Magarusul nu se duce!")
    else:
        print("Magarusul porneste!")
        cate_un_minut=0
        distanta_actuala=0
        #  distanta_actuala+=merge_un_minut(distanta_actuala, dx)
        while(distanta_actuala==finish):
            if distanta_actuala+dx>finish:
                print("S-a trecut pe aici?!")
                dist_ramasa=finish-distanta_actuala
                distanta_actuala+=dist_ramasa
                break
            else:
                cate_un_minut+=1
                trece_un_minut(distanta_actuala)
                distanta_actuala += merge_un_minut(distanta_actuala, dx)
                if cate_un_minut>=n:
                    dx=oboseste_magarusul(dx)
                    cate_un_minut=0
                if distanta_actuala == finish:
                    break
        print("Magarusul a ajuns la finish!")
        print("Magarusul a facut ", distanta_actuala, " in metri!")





if __name__ == '__main__':
    fa_calcule(5, 10, 0)
    print()
    fa_calcule(5, 10, 15)
    print()
    fa_calcule(5, 2, 15)
    print()
    fa_calcule(5,2, 100)
