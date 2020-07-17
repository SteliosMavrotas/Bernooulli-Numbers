from fractions import Fraction
import sys
from decimal import Decimal
def bernoulli_number(n):
    sys.setrecursionlimit(10000) 
    pasc=[[1],[1,1],[1,2,1]]
    brn=[(float(1),float(1)),(float(-1),float(2))]
    
    if n%2!=0 and n!=1:
        return 0
    a=calculateBernouli(n,pasc,brn)[-1]
    
    return Fraction(a[0]/a[1]).limit_denominator(3000)

def calculateBernouli(n,pasc,brn):
    if n==0 or n==1:
        return [[],brn[n]]
    
    pasc.append([1]+[v+pasc[-1][c] for c,v in 
                     enumerate(pasc[-1][1:])]+[1])
    
    if len(pasc)==n+3:
        return brn
    if len(pasc)%2!=0:
        brn.append((0,0))
        return calculateBernouli(n, pasc, brn)
    
    numerator=sum([-1]+[float(-i*y) for i,y in zip([v for c,v in 
                                                    enumerate(pasc[-1][1:len(pasc[-1])-2]) if brn[c+1][1]!=0],
                       [Fraction(brn[c+1][0]/brn[c+1][1]).limit_denominator() for c,v in 
                        enumerate(pasc[-1][1:len(pasc[-1])-2]) if brn[c+1][1]!=0])])
    
    denominator=int(pasc[-1][-2])
    
    brn.append(float.as_integer_ratio(numerator/denominator))
    
    return calculateBernouli(n, pasc, brn)
