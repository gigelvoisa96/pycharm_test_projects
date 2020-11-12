"""
Simplificarea unei fractii rationale p/q
"""
p=int(input("p="))
q=int(input("q="))
d=p
i=q
r=i
while r!=0:
    r=d%i
    d=i
    i=r
print(p, "/", q, " = ", p//d, "/", q//i)