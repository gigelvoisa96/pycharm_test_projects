# Calculul lui n!

def generate_n_factorial():
    n=int(input("n="))
    f=1
    for i in range(1,n+1):
        f=f*i
    print(n, "!=", f)


if __name__ == '__main__':
    nxt=0
    while(True):
        generate_n_factorial()
        nxt=nxt+1
        if nxt == 3:
            break

