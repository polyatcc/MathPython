import math

fibConstFirst = (1.0 + math.sqrt(5)) / 2
fibConstSecond = (1.0 - math.sqrt(5)) / 2


def NthNumberFib(n):
    return int((math.pow(fibConstFirst, n) - math.pow(fibConstSecond, n)) / math.sqrt(5))


def fibonacci(f, a, b, eps):
    count = 0
    v = 0
    list = []

    while (b - a) >= (eps * NthNumberFib(count + 2)):
        count += 1


    NF = NthNumberFib(count)
    NOneF = NthNumberFib(count + 1)
    NTwoF = NthNumberFib(count + 2)
    x1 = a + NF / NTwoF * (b - a)
    x2 = a + NOneF / NTwoF * (b - a)
    y1 = f(x1)
    y2 = f(x2)
    v += 2
    list.append((b, a))
    for i in range(2, count):
        if y1 > y2:
            a = x1
            x1, y1 = x2, y2
            x2 = a + NthNumberFib(count - i + 2) / NthNumberFib(count - i + 3) * (b - a)
            y2 = f(x2)
            v += 1
        else:
            b = x2
            x2, y2 = x1, y1
            x1 = a + NthNumberFib(count - i + 1) / NthNumberFib(count - i + 3) * (b - a)
            y1 = f(x1)
            v += 1
        list.append((b, a))

    min_x = a
    min_y = f(a)
    return min_x, count - 2, v, list


def c(x):
    return math.log(x, 10) * math.sin(x) * x ** 2


i = 0.000001
'''
for j in range(9):
    print(i)
    print(fibonacci(c, 0, 1, i))
    i /= 10
'''
print(fibonacci(c, 0, 1, i))
