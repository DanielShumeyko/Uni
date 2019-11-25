import numpy as np

x0 = 0
y0 = 0
# function is x^2 + xy
def func(x, y):
    return x**2 + x*y

def runge_kutta(n, h):
    y_prev = y0
    x_prev = x0
    outp = []
    outp.append((x_prev,y_prev))
    
    for _ in range(n):
        k1 = h*func(x_prev, y_prev)
        k2 = h*func(x_prev + h, y_prev + k1)
        y = y_prev + (1/2)*k1 + (1/2)*k2
        x = x_prev + h
        outp.append((x, y))
        y_prev = y
        x_prev = x

    return outp

def print_outp(outp):
    str = ''
    i = 0
    for pair in outp:
        str += 'x{}: {}, y{}: {} \n'.format(i, pair[0], i, pair[1])
        i += 1
    return str

print(print_outp(runge_kutta(10, 0.5)))