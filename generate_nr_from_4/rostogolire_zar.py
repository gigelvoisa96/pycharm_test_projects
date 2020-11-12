"""Rostogolire zar"""
def rostogolire_stanga(k):
    global sus,jos,dreapta, stanga, fata, spate
    for i in range(0,k):
        sus,jos, dreapta, stanga=dreapta, stanga, jos, sus
def rostogolire_dreapta(k):
    # global sus, jos, dreapta, stanga, fata, spate
    for i in range(0,k):
        sus,jos,dreapta, stanga=stanga, dreapta, sus, jos
def rostogolire_fata(k):
    # global sus, jos,dreapta, stanga, fata, spate
    for i in range(0,k):
        sus,jos, fata, spate = spate, fata, sus, jos
def rostogolire_spate(k):
    # global sus, jos, dreapta, stanga, fata, spate
    for i in range(0,k):
        sus,jos,fata, spate=fata, spate, jos, sus
print('Dati pozitia initiala a zarului:')
sus=eval(input('Sus='))
fata=eval(input('Fata='))
dreapta=eval(input('Dreapta='))
jos=7-sus
spate=7-fata
stanga=7-dreapta
while True:
    dir=str(input('Directia?(st, dr, fa, sp)'))
    k=int(input('Numar rostogolire'))
    if dir == 'st':
        rostogolire_stanga(k)
    if dir == 'dr':
        rostogolire_dreapta(k)
    if dir == 'fa':
        rostogolire_fata(k)
    if dir == 'sp':
        rostogolire_spate(k)
    print('Pozitia zarului este:')
    print('Sus=', sus)
    print('Jos=', jos)
    print('Fata=', fata)
    print('Spate=', spate)
    print('Stanga=', stanga)
    print('Dreapta=', dreapta)
    cont=str(input(('Continuați?(d/n)')))
    if(cont=='N') or (cont=='n'):
        break

