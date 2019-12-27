
#laba3

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
a, b, c, d = map(int, input().split())
x = a * d
y = b * c
t = gcd(x, y)
print(x // t, '/', y // t, sep='')



