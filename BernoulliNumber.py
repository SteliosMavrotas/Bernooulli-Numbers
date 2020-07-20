from fractions import Fraction
import sys
from decimal import Decimal
def bernoulli_number(n):
    
    sys.setrecursionlimit(10000) 
    pasc=[[1],[1,1],[1,2,1]]
    brn=[Fraction(1),Fraction(-1/2)]
    
    if n%2!=0 and n!=1:
        return 0
    a=calculateBernouli(n,pasc,brn)[-1]
    
    return Fraction(a).limit_denominator()

def calculateBernouli(n,pasc,brn):
    if n==0 or n==1:
        return [[],brn[n]]
    
    pasc.append([1]+[v+pasc[-1][c] for c,v in 
                     enumerate(pasc[-1][1:])]+[1])
    
    if len(pasc)==n+3:
        return brn
    if len(pasc)%2!=0:
        brn.append(0)
        return calculateBernouli(n, pasc, brn)
    
    p,d=[],[]
    
    for c,v in enumerate(pasc[-1][1:len(pasc[-1])-2]):
        p.append(v)
        d.append(brn[c+1])
    
    numerator=sum([-1]+[-i*y for i,y in zip(p,d)])
    
    
    denominator=int(pasc[-1][-2])
    
    brn.append(Fraction(numerator/denominator))
    
    return calculateBernouli(n, pasc, brn)
