

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x_final = np.array([5, 0, 0])
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
        self.t_range = self.t_range[:self.ko]
        self.A = np.matrix([[0, 1, 0], [0, 0, 1], [-1, -self.a1, -self.a2]])
        self.B = np.array([[0, 0, self.b]])
        self.C = np.array([1, 0, 0])

    # Runs algorithm, plots results
    def runModel(self):
        sns.set()
        self.generateY()
        y = self.y1
        x = self.t_range
        plt.xlabel('t - time')
        plt.ylabel('y(t) - output process')
        plt.plot(x, y)
        plt.plot(x, self.y2, c='red')
        plt.plot(x, self.y3, c='green')
        plt.plot(x, self.uk, c='yellow')
        plt.legend(['x1', 'x2', 'x3', 'u(k)'], loc=4)
        plt.show()

    # Algorithm core, loads three y arrays into class
    def generateY(self):
        phi = np.squeeze(np.array(self.Phi()))
        gamma = np.squeeze(self.Gamma(self.Phi()))
        l0 = self.l0()
        y = []
        y2 = []
        y3 = []
        uk = []
        num_of_iters = len(self.t_range)
        x = np.array([])
        x_prev = np.squeeze(self.xo)
        uk.append(0)
        y.append(x_prev[0])
        y2.append(x_prev[1])
        y3.append(x_prev[2])
        for k in range(1, num_of_iters):
            u = np.asscalar(self.U(k-1, l0))
            x = phi.dot(x_prev) + gamma*u
            uk.append(u)
            y.append(x.dot(self.C))
            y2.append(x[1])
            y3.append(x[2])
            x_prev = x
        self.uk = uk
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
    
    def Phi_inv(self):
        phi = np.matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
        q = self.q
        m = -1
        for i in range(q):
           phi += m*((self.A*self.to)**(i+1))/np.math.factorial((i+1))
           m *= -1
        return phi       

    # calculates Gamma to use in main formula, needs Phi
    def Gamma(self, phi):
        I = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        a =  (phi - I)*self.A**(-1)
        a1 = np.squeeze(np.array(a))
        b = np.squeeze(np.array(self.B))
        return a1.dot(b)
        
    def U(self, k, l0):
        return self.G(k).dot(np.transpose(l0))

    def l0(self):
        Pi = np.linalg.matrix_power(self.Phi(), self.ko-1)
        Sigma = 0
        for j in range(0,self.ko):
            Sigma = Sigma + self.G(j).dot(np.transpose(self.G(j)))

        Sigma = np.asscalar(Sigma)
        L = np.linalg.inv(Pi*Sigma)
        return L.dot(x_final)       
            

    def G(self, j):
        gamma = self.Gamma(self.Phi())
        P = np.linalg.matrix_power(self.Phi_inv(), j)
        return P.dot(gamma)


    # for debuging and testing purposes
    def printData(self):
        print('A ', self.A)
        print('B ', self.B)
        print('C ', self.C)
        print('T ', self.t_range)
        phi = self.Phi()
        print('Phi ', phi)
        print('Gamma ', self.Gamma(phi))

