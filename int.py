import math


def gold_section(f, a, b, eps):
    list = []
    count = 0
    v = 0
    const = (3 - math.sqrt(5)) / 2
    x1 = a + const * (b - a)
    x2 = b - const * (b - a)
    y1 = f(x1)
    y2 = f(x2)
    v += 2
    list.append((a, b))
    while abs(b - a) > eps:
        count += 1
        if y1 < y2:
            b = x2
            x2, y2 = x1, y1
            x1 = a + const * (b - a)
            y1 = f(x1)
            v += 1
            list.append((a, b))
        else:
            a = x1
            x1, y1 = x2, y2
            x2 = b - const * (b - a)
            y2 = f(x2)
            v += 1
            list.append((a, b))
    return (x1 + x2) / 2, count, v, list


def a(x):
    return math.log(x, 10) * math.sin(x) * x ** 2

'''
i = 0.1

for j in range(9):
    print(i)
    print(gold_section(a, 0, 1, i))
    i /= 10
'''
j = 0.000001
print(gold_section(a, 0, 1, j))


