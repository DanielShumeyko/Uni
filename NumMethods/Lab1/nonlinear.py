import numpy as np

# This function is basically the function f(x) on the left side of the equation. Here 'nlf' stands for nonlinear function.
def nlf(x):
    return x**3 + np.sin(x) - 12*x + 1

# This is the derivative function of our nlf
def der(x):
    return 3*x**2 + np.cos(x) - 12
class Modified_Newton:
    def __init__(self, eps, a, b, x0):
            self.eps = eps
            self.a0 = a
            self.b0 = b
            self.x0 = x0
    
    def run(self):
        der_x0 = der(self.x0)
        x_prev = self.x0
        i = 1
        log = 'Iteration starting... \nStep 0: a = {}, b = {}, x = {} \n'.format(self.a0, self.b0, self.x0)
        while True:
            x = x_prev - nlf(x_prev) / der_x0
            log += 'Step {}: x = {} \n'.format(i, x)

            if x < self.a0 or x > self.b0:
                log += 'x outside of range, not converging on x*. Stopping iteration.'
                return x, log

            if np.absolute(x - x_prev) <= self.eps:
                log += 'Stop condition met! {} steps completed. \nReturning x = {} \n'.format(i + 1, x)
                return x, log

            x_prev = x
            i += 1


class Dichotomy:
    def __init__(self, eps, a, b):
        self.eps = eps
        self.a0 = a
        self.b0 = b

    def run(self):
        a = self.a0
        b = self.b0
        x_prev = (a + b)/2
        x = 0
        i = 1
        log = 'Iteration starting... \nStep 0: a = {}, b = {}, x = {} \n'.format(a, b, x)

        while True:
            if nlf(a) * nlf(x_prev) > 0:
                a = x_prev
            if nlf(b) * nlf(x_prev) > 0:
                b = x_prev
            x = (a + b)/2
            log += 'Step {}: a = {}, b = {}, x = {} \n'.format(i, a, b, x)
            if np.absolute(x - x_prev) <= self.eps:
                log += 'Stop condition met! \n{} steps expected / {} steps completed. \nReturning x = {} \n'.format(self.eval_n(), i + 1, x)
                return x, log
            x_prev = x
            i += 1


    def eval_n(self):
        return (int(np.log2((self.b0 - self.a0)/self.eps)) + 1)

