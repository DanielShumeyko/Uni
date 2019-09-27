# Daniel Shumeyko, PS-3

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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
        self.xo = np.array([xo, xo, xo])
        self.t_range = np.arange(0, 10 + self.to, self.to)
        self.A = np.matrix([[0, 1, 0], [0, 0, 1], [-1, -self.a1, -self.a2]])
        self.B = np.array([[0, 0, self.b]])
        self.C = np.array([1, 0, 0])

    # runs model calculating y values then plots
    def runModel(self):
        sns.set()
        self.generateY()
        y = self.y1
        x = self.t_range
        axes = plt.axes()
        axes.set_xlim([-0.2, 10.2])
        axes.set_xticks(np.arange(0, 10.5, 0.5))
        plt.xlabel('t - time')
        plt.ylabel('y(t) - output process')
        plt.scatter(x, y)
        plt.scatter(x, self.y2, c='red')
        plt.scatter(x, self.y3, c='green')
        plt.legend(['x1', 'x2', 'x3'], loc=4)
        plt.show()

    def generateY(self):
        phi = np.squeeze(np.array(self.Phi()))
        gamma = np.squeeze(self.Gamma(self.Phi()))
        y = []
        y2 = []
        y3 = []
        k = len(self.t_range)
        u = 1
        ucounter = 0
        x = np.array([])
        x_prev = np.squeeze(self.xo)
        y.append(x_prev[0])
        y2.append(x_prev[1])
        y3.append(x_prev[2])

        for _ in range(1, k):
            x = x_prev.dot(phi) + gamma*u
            print(x)
            y.append(x.dot(self.C))
            y2.append(x[1])
            y3.append(x[2])
            x_prev = x
            ucounter += 1
            if self.ko > 0:
                if ucounter >= self.ko:
                    u *= -1
                    ucounter = 0

        self.y1 = y
        self.y2 = y2
        self.y3 = y3

            
        

    # calculates Phi to use in main formula
    def Phi(self):
        phi = np.matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
        q = self.q
        for i in range(q):
            # ((self.A*self.to)**(i+1))/np.math.factorial((i+1))
            phi += ((self.A*self.to)**(i+1))/np.math.factorial((i+1))
        return phi

    # calculates Gamma to use in main formula, needs Phi
    def Gamma(self, phi):
        I = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        a =  (phi - I)*self.A**(-1)
        a1 = np.squeeze(np.array(a))
        b = np.squeeze(np.array(self.B))
        return a1.dot(b)
        

    # for debuging and testing purposes
    def printData(self):
        print('A ', self.A)
        print('B ', self.B)
        print('C ', self.C)
        print('T ', self.t_range)
        phi = self.Phi()
        print('Phi ', phi)
        print('Gamma ', self.Gamma(phi))

# Daniel Shumeyko, PS-3