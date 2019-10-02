import numpy as np

# This function is basically the function f(x) on the left side of the equation. Here 'nlf' stands for nonlinear function.
def nlf(x):
    return x**3 + np.sin(x) - 12*x + 1

class Modified_Newton:
    def __init__(self, eps):
        self.eps = eps
class Dichotomy:
    def __init__(self, eps):
        self.eps = eps