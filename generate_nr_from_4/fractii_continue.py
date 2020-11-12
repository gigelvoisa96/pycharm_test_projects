"""
Fractie continua
p/q=7+2/5=7+1/(5/2)=7+1/(2+1/2)=...
37/5=[7,2,2]
"""
p=eval(input('p='))
q=eval(input('q='))
fc=[]
d=p
i=q
r=1
while r!=0:
    r=d%i
    c=d//i
    fc.append(c)
    d=i
    i=r
print(fc)