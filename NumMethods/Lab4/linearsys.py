import numpy as np

A = np.array([[3, 1, 1],[1, 7, 5],[3, 3, 6]])
b = np.array([1, 3, 2])
Eps = 0.001
x0 = [0, 0, 0]

A_sr =np.array([[1, 2, 3],[2, 5, 5],[3, 5, 6]])
b_sr = np.array([1, 3, 2])

# the definition of bruteforcing and harcoding, scaling isn't even an option, but hey, it works
class Square_Roots:
    def __init__(self):
        pass
    def run(self):
        S = np.array([[0.0, 0.0, 0.0], [0.0, 0.0 , 0.0], [0.0, 0.0, 0.0]])
        D = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        # calculate all elements of D and S, very bruteforce approach but I'm tired
        S[0][0] = A_sr[0][0]
        D[0][0] = np.sign(A_sr[0][0])
        S[0][1] = A_sr[0][1] / (D[0][0] * S[0][0])
        S[0][2] = A_sr[0][2] / (D[0][0] * S[0][0])
        S[1][1] = (np.absolute(A_sr[1][1] - ((S[0][1])**2)*D[0][0]))**(1/2)
        D[1][1] = np.sign(A_sr[1][1] - ((S[0][1])**2)*D[0][0])
        S[1][2] = (A_sr[1][2] - S[0][1]*S[0][2]*D[0][0])/(S[1][1]*D[1][1])
        D[2][2] = np.sign(A_sr[2][2] - ((S[0][2])**2)*D[0][0] - ((S[1][2])**2)*D[1][1])
        S[2][2]= (np.absolute(A_sr[2][2] - ((S[0][2])**2)*D[0][0] - ((S[1][2])**2)*D[1][1]))**(1/2)

        # calculate transposed S matrix multiplied by D
        StD = np.transpose(S).dot(D)
        # calculate y from simple linear system (which is always triangular which is why this is possible)
        y = []
        y.append(StD[0][0]/b_sr[0])
        y.append((b_sr[1] - StD[1][0]*y[0])/StD[1][1])
        y.append((b_sr[2]- StD[2][0]*y[0] - StD[2][1]*y[1])/StD[2][2])

        # now we calculate our x, same approach as above but in reverse order:

        x = [0, 0, 0]
        x[2] = y[2] / S[2][2]
        x[1] = (y[1] - S[1][2]*x[2])/S[1][1]
        x[0] = (y[0]- S[0][1]*x[1]- S[0][2]*x[2])/S[0][0]
        
        log = 'S: \n' + str(S) + '\nD: \n' + str(D) + '\ny: \n'+ str(y) + '\nx: \n' + str(x) + '\ndet: \n' + str(self.det(S, D)) + '\nM: \n' + str(self.M(A_sr))
        return log

    def matrix_symmetrical(self, A=A_sr):
        tested = A - np.transpose(A)
        for row in tested:
            for element in row:
                if not element == 0:
                    return False
        return True
    
    def det(self, S, D):
        det = 1
        for i in range(3):
            det *= D[i][i] * (S[i][i]**2)
        return det
    
    def M(self, A):
        return np.linalg.norm(A, ord=1)*(np.linalg.norm(A[::-1],ord=1))
        
# Seidel method for solving linear systems
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
                log += 'Stop condition met! \n x = {} is the solution\n'.format(str(x))
                break
            x_prev = x
            x = []
        log += 'M: {}'.format(str(self.M(A)))
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

    def M(self, A):
        return np.linalg.norm(A, ord=1)*(np.linalg.norm(A[::-1],ord=1))

test = Square_Roots()
test.run()