# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:43:03 2020

@author: я
"""

def Parabola(x):
    return x**2
def Line(x):
    return 2*x
def NegParabola(x):
    return -x**2-5
# A, B = -5, 5

def Extremum(A,B, *, func, **kargs):
    a = [func(x) for x in range(A,B)]
    print(a)
    d = max(zip(a, range(len(a))))
    c = min(zip(a, range(len(a))))
    r = c[0],d[0]
    w = a[0],a[len(a)-1]
    zero = set()
    dif = set(r) - set(w)
    if dif == zero:
        dif = None
    return dif
   
result = Extremum(-2, 2, func=Parabola)
result1 = Extremum(-20, -10, func=Parabola)
result2 = Extremum(-2, 2, func=Line)
result3 = Extremum(-2, 2, func=NegParabola)
print("Extremum at:",result1)
print("Extremum at:",result)
print("Extremum at:",result2)
print("Extremum at:",result3)


