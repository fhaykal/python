print 'Hello, world!'
import numpy
def somdiv(n):
    s=0
    for i in range(1,n):
        if n%i==0:
          s=s+i
    return s

for j in range (1,10000):
    if somdiv(j)==j:
        print(j)
        
def parfait(n):
    return somdiv(n)==n  #bool true or false
