# Daniel Shumeyko, PS-3

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class DynamicModel:
    def __init__(self, a1, a2, b, q, t, ko, xo, l2, l3):
        self.changeData(a1, a2, b, q, t, ko, xo, l2, l3)
    
    # just loads new data into the model
    def changeData(self, a1, a2, b, q, t, ko, xo, l2, l3):
        self.a1 = a1
        self.a2 = a2
        self.b = b
        self.q = q
        self.to = t
        self.ko = ko
        self.xo = np.array([xo, xo, xo])
        self.delta_l2 = l2
        self.delta_l3 = l3
        self.t_range = np.arange(0, 10 + self.to, self.to)
        self.A = np.matrix([[0, 1, 0], [0, 0, 1], [-1, -self.a1, -self.a2]])
        self.B = np.array([[0, 0, self.b]])
        self.C = np.array([1, 0, 0])
        self.l = np.array([0, 0, 0])

    # Runs algorithm, plots results
    def runModel(self):
        sns.set()
        self.calculate_l()
        self.generateY(self.l)
        y = self.y1
        x = self.t_range
        axes = plt.axes()
        axes.set_xlim([-0.2, 10.2])
        axes.set_xticks(np.arange(0, 10.5, 0.5))
        plt.xlabel('t - time')
        plt.ylabel('y(t) - output process')
        plt.scatter(x, y)
        plt.show()

    # Algorithm core, loads three y arrays into class
    def generateY(self, l=np.array([0, 0, 0])):
        self.y1 = []
        self.y2 = []
        self.y3 = []
        phi = np.squeeze(np.array(self.Phi()))
        gamma = np.squeeze(self.Gamma(self.Phi()))
        y = []
        y2 = []
        y3 = []
        k = len(self.t_range)
        u = 1
        x = np.array([])
        x_prev = np.squeeze(self.xo)
        y.append(x_prev[0])
        y2.append(x_prev[1])
        y3.append(x_prev[2])
        print('l:' + str(l))
        print('gamma: ' + str(gamma))
        print('gamma*l: ' + str(gamma.dot(l)) )
        for _ in range(1, k):
            x = x_prev.dot(phi - gamma.dot(l)) + gamma*u # TODO: Instead of Phi there should be Phi - Gamma*l^T
            y.append(x.dot(self.C))
            y2.append(x[1])
            y3.append(x[2])
            x_prev = x

        self.y1 = y
        self.y2 = y2
        self.y3 = y3

            
        

    # calculates Phi to use in main formula
    def Phi(self):
        phi = np.matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
        q = self.q
        for i in range(q):
            phi += ((self.A*self.to)**(i+1))/np.math.factorial((i+1))
        return phi

    # calculates Gamma to use in main formula, needs Phi
    def Gamma(self, phi):
        I = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        a =  (phi - I)*self.A**(-1)
        a1 = np.squeeze(np.array(a))
        b = np.squeeze(np.array(self.B))
        return a1.dot(b)
    
    #calculates l for current moment k
    def calculate_l(self):
        delta_l2 = self.delta_l2
        delta_l3 = self.delta_l3
        l = np.array([0.0, 0.0, 0])
        if delta_l2 == 0:
            self.generateY(l)
            J_prev = 0
            for item in self.y1:
                J_prev += np.absolute(item - 1)*self.to
            while True:
                l[2] = l[2] + delta_l3
                print('changed l: ' + str(l))
                J = 0
                self.generateY(l)
                for item in self.y1:
                    J += np.absolute(item - 1)*self.to
                print(J)
                if J_prev - J < 0:
                    delta_l3 *= -1
                    continue
                if J < 0.1:
                    print("Finished")
                    break
                J_prev = J
            print('Final l  = ' + str(l))
            self.l = l

        else:
            self.generateY(l)
            J_prev = 0
            for item in self.y1:
                J_prev += np.absolute(item - 1)*self.to
            while True:
                l[2] = l[2] + delta_l2
                print('changed l: ' + str(l))
                J = 0
                self.generateY(l)
                for item in self.y1:
                    J += np.absolute(item - 1)*self.to
                print(J)
                if J_prev - J < 0:
                    delta_l2 *= -1
                    continue
                if J < 0.1:
                    print("Finished")
                    break
                J_prev = J
            print('Final l  = ' + str(l))
            self.l = l
            

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