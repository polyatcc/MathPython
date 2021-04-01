import math


def midPoint (f, x1, x2, y1, y2):
    while True:
        x = (x1 + x2) / 2
        y = f(x)
        if y <= y1 and y <= y2:
            return (x, y)
        elif y > y1:
            x2 = x
            y2 = y
        elif y > y2:
            x1 = x
            y1 = y


def parabolic(f, a, b, eps):
    list = []
    count = 0
    v = 0
    y1 = f(a)
    y2 = f(b)
    x, y = midPoint(f, a, b, y1, y2)
    ex = 0
    now = 1
    while abs(now - ex) > eps:
        ex = now
        nowX = 0.5 * (a + x - ((y - y1) * (b - x) / (x - a) / ((y2 - y1) / (b - a) - (y - y1) / (x - a))))
        nowY = f(nowX)
        if x < nowX:
            if y < nowY:
                b = nowX
                y2 = nowY
            else:
                a = x
                y1 = y
                x = nowX
                y = nowY
        else:
            if nowY < y:
                b = x
                y2 = y
                x = nowX
                y = nowY
            else:
                a = nowX
                y1 = nowY
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
print(parabolic(a, 0.000000001, 1, i))