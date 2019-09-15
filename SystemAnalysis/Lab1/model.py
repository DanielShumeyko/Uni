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
        self.xo = np.array([xo, xo, xo])
        self.t_range = np.arange(0, 10 + self.to, self.to)
        self.A = np.matrix([[0, 1, 0], [0, 0, 1], [-1, -self.a1, -self.a2]])
        self.B = np.array([[0, 0, self.b]])
        self.C = np.array([1, 0, 0])

    # runs model calculating y values then plots
    def runModel(self):
        y = self.generateY()
        axes = plt.axes()
        axes.grid()
        print(len(y))
        print(len(self.t_range))
        plt.plot(self.t_range, y, color='olive', zorder=3)
        plt.show()

    def generateY(self):
        phi = np.squeeze(np.array(self.Phi()))
        gamma = np.squeeze(self.Gamma(phi))
        y = []
        k = len(self.t_range)
        u = 1
        ucounter = 0
        x = np.array([])
        x_prev = np.squeeze(self.xo)

        y.append(x_prev[0])

        for i in range(1, k):
            x = phi.dot(x_prev) + gamma*u
            y.append(x[0])
            x_prev = x
            ucounter += 1
            if ucounter >= self.ko:
                u *= -1
                ucounter = 0
        return y
            
        

    # calculates Phi to use in main formula
    def Phi(self):
        phi = np.matrix([[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]])
        q = self.q
        for i in range(q):
            # ((self.A*self.to)**(i+1))/np.math.factorial((i+1))
            phi += ((self.A*self.to)**(i+1))/np.math.factorial((i+1))
        return phi

    # calculates Gamma to use in main formula, needs Phi
    def Gamma(self, phi):
        I = np.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
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
