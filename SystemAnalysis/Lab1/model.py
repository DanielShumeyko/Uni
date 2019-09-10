import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class DynamicModel:
    def __init__(self, a1, a2, b, q, t):
        self.changeData(a1, a2, b, q, t)
    
    # just loads new data into the model
    def changeData(self, a1, a2, b, q, t):
        self.a1 = a1
        self.a2 = a2
        self.b = b
        self.q = q
        self.to = t
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

    # for debuging and testing purposes
    def printData(self):
        print(self.A)
        print(self.B)
        print(self.C)
        print(self.t_range)
