import numpy as np

# This function is basically the function f(x) on the left side of the equation. Here 'nlf' stands for nonlinear function.
def nlf(x):
    return x**3 + np.sin(x) - 12*x + 1

# This is the derivative function of our nlf
def der(x):
    return 3*x**2 + np.cos(x) - 12
class Modified_Newton:
    def __init__(self, eps):
        self.eps = eps
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
                break
            x_prev = x
            i += 1
        return x, log

    def eval_n(self):
        return (int(np.log2((self.b0 - self.a0)/self.eps)) + 1)