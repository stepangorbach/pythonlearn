#1.Определить, имеется ли среди чисел a b c хотя бы одна пара взаимно противоположных чисел.
#2.Известно, что из четырех чисел a1 a2 a3 a4 одно отлично от трех других, равных между собой. Присвоить номер этого числа переменной n
#3.Даны два прямоугольника на координатной плоскости, стороны которых параллельны или перпендикулярны координатным осям. Известны координаты левого нижнего угла каждого прямоугольника и длины их сторон. Найти координаты левого верхнего и правого нижнего углов минимального по площади прямоугольника, содержащего указанные прямоугольники.
#4.Даны объемы и массы двух тел из разных материалов. Определить, плотность какого тела больше.


def zadanie1():
    a = int(input("введите число 1 "))
    b = int(input("введите число 2 "))
    c = int(input("введите число 3 "))
    if a + b == 0 and a != b:
        print("число a ", a, " и  число b ", b, " взаимно противоположны ")
    elif b + c == 0 and b != c:
        print("число b ", b, " и  число c ", c, " взаимно противоположны")
    elif a + c == 0 and a != c:
        print("число a ", a, " и  число c ", c, " взаимно противоположны")
    else:
        print("нет взаимно противоположных чисел")

zadanie1()

def zadanie2():
    n = 0 
    a1 = int(input("введите число 1 "))
    a2 = int(input("введите число 2 "))
    a3 = int(input("введите число 3 "))
    a4 = int(input("введите число 4 "))
    if a2 + a3 + a4 != 3*a1 and a2 + a3 + a4 == 3*a2:
        n = 1
        print("число a1 отлично от других, n = ", n) 
    elif a1 + a3 + a4 != 3*a2 and a1 + a3 + a4 == 3*a1:  
        n = 2
        print("число a2 отлично от других, n = ", n)
    elif a1 + a2 + a4 != 3*a3 and a1 + a2 + a4 == 3*a1:
        n = 3
        print("число a3 отлично от других, n = ", n)
    elif a1 + a2 + a3 != 3*a4 and a1 + a2 + a3 == 3*a1:
        n = 4
        print("число a4 отлично от других, n = ", n)          
    else:
        print("нет отличных чисел")

zadanie2()

def zadanie3():
    s = 0
    a1 = [0, 0]; a2 = [0, 0]
    a3 = [0, 0]; a4 = [0, 0]
    b1 = [0, 0]; b2 = [0, 0]
    b3 = [0, 0]; b4 = [0, 0]
    big1 = [0, 0]; big2 = [0, 0]
    big3 = [0, 0]; big4 = [0, 0]
    h1w1 = [0, 0]; h2w2 = [0, 0]; h3w3 = [0, 0]
    a4[0] = int(input("")); a4[1] = int(input(""))
    b4[0] = int(input("")); b4[1] = int(input(""))
    h1w1[0] = abs(int(input(""))); h1w1[1] = abs(int(input("")))
    h2w2[0] = abs(int(input(""))); h2w2[1] = abs(int(input("")))
    print(h1w1, h2w2)
    a1[1] = a4[1] + h1w1[0]; a1[0] = a4[0] 
    a2[0] = a1[0] + h1w1[1]; a2[1] = a1[1]
    a3[0] = a4[0] + h1w1[1]; a3[1] = a4[1]
    print(a1, a2, a3, a4)
    b1[1] = b4[1] + h2w2[0]; b1[0] = b4[0] 
    b2[0] = b1[0] + h2w2[1]; b2[1] = b1[1]
    b3[0] = b4[0] + h2w2[1]; b3[1] = b4[1]
    print(b1, b2, b3, b4)
    if a3[0] >= b3[0]:
        big3[0] = a3[0] 
    else: 
        big3[0] = b3[0]

    if a3[1] <= b3[1]:
        big3[1] = a3[1] 
    else: 
        big3[1] = b3[1] 

    if a4[0] <= b4[0]:
        big3[0] = a3[0] 
    else: 
        big4[0] = b4[0]
    big4[1] = big3[1]; big1[0] = big4[0] 

    if a1[1] >= b1[1]:
        big1[1] = a1[1] 
    else: 
        big1[1] = b1[1]
    big2[0] = big3[0]; big2[1] = big1[1]
    print(big1, big2, big3, big4)
    if big1[0] < 0 and big2[0] >= 0: 
        h3w3[0] = abs(big1[0]) + abs(big2[0])
    elif big1[0] < 0 and big2[0] < 0: 
        h3w3[0] = abs(big1[0]) - abs(big2[0])
    else: 
        h3w3[0] = abs(big2[0]) - abs(big1[0])
    
    if big4[1] < 0 and big1[1] >= 0: 
        h3w3[1] = abs(big4[1]) + abs(big1[1])
    elif big4[1] < 0 and big1[1] < 0: 
        h3w3[1] = abs(big4[1]) - abs(big1[1])
    else: 
        h3w3[1] = abs(big1[1]) - abs(big4[1])

    print(h3w3)
    s = h3w3[0]*h3w3[1]
    print(s)
zadanie3()

def zadanie4():
    v1 = float(input()); v2 = float(input())
    m1 = float(input()); m2 = float(input())
    if (m1/v1) > (m2/v2):
        print("плотность тела 1 больше")
    else:
        print("плотность тела 2 больше")
zadanie4()




