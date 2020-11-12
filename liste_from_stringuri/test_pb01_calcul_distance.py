def deplasare_cu_un_minut(actuala_distanta_parcurs, pas):
    actuala_distanta_parcurs+=pas



def calculare_distanta_traseu_magarus(nr_de_metri_pe_minut, n_minute_de_jumatatire, final_de_distanta):
    print("nr_de_metri_pe_minut: ",nr_de_metri_pe_minut)
    print("n_minute_de_jumatatire: ", n_minute_de_jumatatire)
    print("final_de_distanta: ", final_de_distanta)
    if nr_de_metri_pe_minut<1:
        print("Magarusul nu o sa porneasca la drum!")
        return
    else:
        print("Magarusul a pornit la drum!")
        actuala_distanta_parcursa=0
        deplasament_de_un_minut=0
        print("Se porneste de la minutul ", deplasament_de_un_minut)
        while(actuala_distanta_parcursa<=final_de_distanta):
            deplasare_cu_un_minut(actuala_distanta_parcursa, nr_de_metri_pe_minut, deplasament_de_un_minut)
            if deplasament_de_un_minut==n_minute_de_jumatatire:
                pas=pas/2


if __name__ == '__main__':
    calculare_distanta_traseu_magarus(nr_de_metri_pe_minut=5, n_minute_de_jumatatire=10, final_de_distanta=100.00)