import numpy as np

# function is ln(x), approx integral on [1;10] is 14.02585
a = 1
b = 10
Eps = 0.01

def func(x):
    return np.log(x)

def left_rectangles():
    h = 1
    I_prev = 0
    steps = 0
    while True:
        slices = np.arange(a, b + h, h)
        I = 0
        for slice in slices:
            I += func(slice)*h
        steps += 1
        if np.absolute(I - I_prev) <= Eps:
            return I, h, steps
        else:
            I_prev = I
            h /= 2

I, h, steps = left_rectangles()
print('I: ' + str(I))
print('Final h: ' + str(h))
print('Iterations: ' + str(steps))
