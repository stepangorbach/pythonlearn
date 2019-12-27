from random import random as miniRandom
from random import randint as random

def factorial(x):
    factDef = 1
    for i in range(1, x+1):
        factDef = factDef*i
    return(factDef)

def task1():
    n = 1; num = float(1); sumNum = 0
    e = miniRandom()
    print("e: ", e)
    while True:
        num = 10**n/factorial(n)
        if abs(num) > abs(e):
            sumNum += num
            print("num: ", num, "sum: ", sumNum)
        else:
            print("num: ", num)

        if abs(num) < abs(e):
            break

        n += 1
    print("Сумма равна: ", sumNum)
    print("\n\n\n")

task1()

def task2(n):
    num = 0; s = 0
    for i in range(1, n+1):
        if i%2 == 0:
            num = 1/2**i
        else:
            num = (-1)*(1/2**i)
        s += num
        print("num: ", num, "   sum: ", s)

task2(int(input("Введите число: ")))

def task3(n):
    num = 0; s = 0
    for i in range(1, n+1):
        num = factorial(i)**(1/(2**i))
        s += num
        print("num: ", num, "sum: ", s)
task3(int(input("Введите число: ")))

#helloworld!



