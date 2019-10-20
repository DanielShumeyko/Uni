import numpy as np

A = np.matrix([[3, 1, 1],[1, 7, 5],[3, 3, 6]])
b = np.array([1, 3, 2])
Eps = 0.001
x0 = [0, 0, 0]



class Square_Roots:
    pass

class Seidel:
    def __init__(self, A=A, b=b, Eps=Eps, x0=x0):
        self.A = A
        self.b =b
        self.Eps = Eps
        self.x0 = x0

    def run(self):
        counter = 1
        x_prev = x0
        x = []
        log = 'Checking matrix A before starting algorithm...\n'
        if not self.matrix_valid():
            log += 'Matrix invalid, couldn\'t start algorithm.\n'
            return log
        log += 'Matrix valid, starting algorithm.\n'
        log += 'Step 0: x = ' + str(x_prev) + '\n'
        while True:
            for k in range(0,3):
                xk = 0
                for i,item in enumerate(x):
                    xk -= A[k,i]/A[k,k]*item
                for i, item in enumerate(x_prev[k+1:]):
                    xk -= A[k,i]/A[k,k]*item
                xk += b[k]/A[k,k]
                x.append(round(xk,5))
            log += 'Step {}: x = {} \n'.format(counter,str(x))
            counter += 1
            if self.stop_condition(x, x_prev, Eps):
                log += 'Stop condition met! \n x = {} is the solution'.format(str(x))
                break
            x_prev = x
            x = []
        return log

    def matrix_valid(self):
        for i in range(3):
            akk = np.absolute(A[i,i])
            a_other = 0
            for k in range(3):
                a_other += np.absolute(A[i,k])
            a_other -= akk

            if akk < a_other:
                return False
        return True

    def stop_condition(self, x, x_prev, eps):
        x_new = []
        for i in range(3):
            x_new.append(np.absolute(x[i] - x_prev[i]))
        if max(x_new) <= eps:
            return True
        else:
            return False


