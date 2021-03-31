import math


def dichotomy(f, a, b, eps):
    list = []
    count = 0
    v = 0
    while abs(b - a) > eps:
        count += 1
        x1 = (b + a) / 2 - eps / 4
        x2 = (b + a) / 2 + eps / 4
        if f(x1) == f(x2):
            v += 2
            a = x1
            b = x2
            list.append({a, b})
            continue
        if f(x1) > f(x2):
            a = x1
        else:
            b = x2
        v += 2
        list.append({a, b})
    return (a + b) / 2, count, v, list


def a(x):
    return math.log(x, 10) * math.sin(x) * x ** 2


i = 0.000001
'''
for j in range(9):
    print(i)
    print(dichotomy(a, 0, 1, i))
    i /= 10
'''
print(dichotomy(a, 0, 1, i))
