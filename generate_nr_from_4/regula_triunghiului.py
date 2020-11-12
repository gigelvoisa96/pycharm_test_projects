"""Rezolvarea triunghiului, se dau laturile a,b,c"""
from math import *

from numpy.lib.scimath import arccos

a=eval(input("a="))
b=eval(input("b="))
c=eval(input("c="))
p=(a+b+c)/2
P=2*p
S=sqrt(p*(p-a)*(p-b)*(p-c))
r=S/p
R=a*b*c/(4*S)
A=acos((b**2+c**2-a**2)/(2*b*c))
B=acos((a**2+c**2-b**2)/(2*a*c))
C=acos((a**2+b**2-c**2)/(2*a*b))
print("Unghiul A este: ", format(A, '.2f'))
print("Unghiul B este: ", format(A, '.2f'))
print("Unghiul C este: ", format(A, '.2f'))
print("Suprafata triunghiului este: ", format(S, '.2f'))
print("Perimetrul triunghiului este: ", format(P, '.2f'))
print("Raza cercului circumscris ", format(R, '.2f'))
print("Raza cercului inscris este: ", r)
print("Unghiul A in grade este: ", format(degrees(A)), '.2f')
print("Unghiul B in grade este: ", format(degrees(B)), '.2f')
print("Unghiul C in grade este: ", format(degrees(C)), '.2f')

