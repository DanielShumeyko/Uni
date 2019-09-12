import matplotlib.pyplot as plt
import numpy as np

class DynamicModel:
    def __init__(self, a1, a2, b, q, t, ko, xo):
        self.changeData(a1, a2, b, q, t, ko, xo)
    
    # just loads new data into the model
    def changeData(self, a1, a2, b, q, t, ko, xo):
        self.a1 = a1
        self.a2 = a2
        self.b = b
        self.q = q
        self.to = t
        self.ko = ko
        self.xo = xo
        self.t_range = np.arange(0, 10 + self.to, self.to)
        self.A = np.matrix([[0, 1, 0], [0, 0, 1], [-1, -self.a1, -self.a2]])
        self.B = np.matrix([[0, 0, self.b]])
        self.C = np.array([1, 0, 0])

    # runs model calculating y values then plots
    def runModel(self):
        self.y = [(self.a1 * t ** self.q + self.a2 * t ** self.b) for t in self.t_range]
        axes = plt.axes()
        axes.grid()
        plt.bar(self.t_range, self.y, color='olive', zorder=3)
        plt.show()

    # calculates Phi to use in main formula
    def Phi(self):
        pass

    # calculates Gamma to use in main formula, needs Phi
    def Gamma(self, phi):
        pass

    # for debuging and testing purposes
    def printData(self):
        print(self.A)
        print(self.B)
        print(self.C)
        print(self.t_range)
