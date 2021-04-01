import math

const = (3 - math.sqrt(5)) / 2

def signum(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0

def rapabolicRegex(x1, x2, x3, y1, y2, y3):
    return x2 - 0.5 * (math.pow(x2 - x1, 2) * (y2 - y3) - math.pow(x2 - x3, 2) * (y2 - y1)) / ((x2 - x1) * (y2 - y3) - (x2 - x3) * (y2 - y1))

def brent(f, a, b, eps):
    list = []
    count = 0
    vy = 0
    u = z = v = x = a + const * (b - a)
    fx = fv = fz = f(x)
    vy += 1
    c = e = b - a
    list.append((b, a))
    while c > eps:
        count += 1
        isPar = False
        tmp, e = e, c
        if x != v and x != z and v != z and fx != fv and fx != fz and fv != fz:
            u = rapabolicRegex(x, z, v, fx, fz, fv)
            if a + eps <= u <= b - eps and abs(u - x) < tmp / 2:
                c = abs(u - x)
                isPar = True
        if not isPar:
            if x < (b - a) / 2:
                u, c = x + const * (b - x), b - x
            else:
                u, c = x - const * (x - a), x - a
            if abs(u - x) < eps:
                u = x + signum(u - x) * eps
        fu = f(u)
        vy += 1
        if fu <= fx:
            if u >= x:
                a = x
            else:
                b = x
            v, z, x = z, x, u
            fv, fz, fx = fz, fx, fu
        else:
            if u >= x:
                b = u
            else:
                a = u
            if fu <= fz or z == x:
                v, z, fv, fz = z, u, fz, fu
            elif fu <= fv or v == x or v == z:
                v, fv = u, fu
        list.append((b, a))
    return x, count, vy, list






def a(x):
    return math.log(x, 10) * math.sin(x) * x ** 2


i = 0.000001
'''
for j in range(9):
    print(i)
    print(brent(a, 0, 1, i))
    i /= 10
'''
print(brent(a, 0, 1, i))
