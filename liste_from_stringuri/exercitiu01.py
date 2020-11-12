def calc_distance(x_pe_pas, nr_timp, total_distance):
    #actual_distance:=0
    #
    actual_distance=0
    pas=0
    task=1
    if x_pe_pas<1:
        print("Măgărușul s-a oprit!")
    else:
        print("magarusul parcurge : \nde la:", actual_distance)
        while(x_pe_pas >= 1):
            actual_distance+= x_pe_pas
            pas+=1
            if pas*x_pe_pas >= nr_timp:
                x_pe_pas=x_pe_pas/2
                # pas=0
                task+=1
                nr_timp=task*nr_timp
            print("spre ", actual_distance, "cu pasul ", pas)
            if x_pe_pas==total_distance:
                break
    if actual_distance==total_distance:
        print("Magarusul a ajuns la finish!")



if __name__ == '__main__':
    calc_distance(5,10, 60)