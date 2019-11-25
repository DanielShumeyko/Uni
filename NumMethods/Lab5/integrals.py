import numpy as np

# function is ln(x), approx integral on [1;10] is 14.02585...
a = 1
b = 10
Eps = 0.01
M1 = 1

def func(x):
    return np.log(x)

def left_rectangles():
    h = 1
    I_prev = 0
    steps = 0
    while True:
        slices = np.arange(a, b, h)
        I = 0
        for slice in slices:
            I += func(slice)*h
        steps += 1
        if np.absolute(I - I_prev) <= Eps:
            err = ((b - a)*M1*h)/2
            return I, h, steps, err
        else:
            I_prev = I
            h /= 2

I, h, steps, err = left_rectangles()
print('I: ' + str(I))
print('Final h: ' + str(h))
print('Iterations: ' + str(steps))
print('Error: ' + str(err))
