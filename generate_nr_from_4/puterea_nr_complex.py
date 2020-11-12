"""
Puterea unui numar complex (a+bi)**n
x=a, y=b
(x+yi)(a+bi)=(ax-by)+(ay+bx)*i

(ax-by) --> x=ax-by
(ay+bx) --> t=x --> y=ay+bt

Pseudocod:
Algoritm puterea numar complex
Read a,b,n
x:=a
y:=b
for i=1,n-1
    t:=x
    x:=ax-by
    y:=ay+bt
endfor
write x,y
stop
"""
a=eval(input("a="))
b=eval(input("b="))
n=eval(input("n="))
x=a
y=b
for i in range(1,n):
    t=x
    x=a*x-b*y
    y=a*y + b*t
print("x=",x,'y=', y)
print((a+b*1j)**n)
