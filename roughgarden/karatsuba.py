import math


def karatsuba(x, y):
    if x < 100 or y < 100:
        return x * y
    str_x = str(x)
    str_y = str(y)
    len_x = len(str_x)
    len_y = len(str_y)
    m = max(len_x, len_y)
    m2 = math.floor(m / 2)
    str_x = str_x.rjust(m, '0')
    str_y = str_y.rjust(m, '0')
    a = int(str_x[:m2])
    b = int(str_x[m2:])
    c = int(str_y[:m2])
    d = int(str_y[m2:])
    z2 = karatsuba(a, c)
    z0 = karatsuba(b, d)
    z1 = karatsuba(a + b, c + d) - z2 - z0

    base = 10 ** (m - m2)
    return (base ** 2 * z2) + (base * z1) + z0


a = karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
b = 3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627

print(a)
print(b)
print(a == b)
