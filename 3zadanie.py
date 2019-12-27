#задание 1
from random import randint as random 

def zadanie1(x):
    factDef = 1
    for i in range(1,x+1):
        factDef = factDef*i
    return(factDef)

def sss(y):
    e = random(1,300)
    num = 0 
    s = 0
    print(e) 
    for i in range(1,y+1):
        num = (10 ** i)/zadanie1(i) 
        print((10 ** i)/zadanie1(i))
        if num > e: 
            s += num 
    print(s)

sss(5)        
