import numpy as np

x0 = [0, 0]
Eps = 0.001

def nls(x_vec):
    x = x_vec[0]
    y = x_vec[1]
    outp = []
    outp.append(x - (1/2)*np.sin((x-y)/2))
    outp.append(y - (1/2)*np.cos((x+y)/2))
    return outp

def calc_A(x_vec):
    x = x_vec[0]
    y = x_vec[1]
    A = np.array([[0.0, 0.0], [0.0, 0.0]])
    A[0][0] = 1 - (1/4)*np.cos((x - y)/2)
    A[0][1] = (1/4)*np.cos((x-y)/2)
    A[1][0] = (1/4)*np.sin((x+y)/2)
    A[1][1] = 1 + (1/4)*np.sin((x+y)/2)
    return A
    

class Newton:
    def __init__(self):
        pass
    def run(self):
        x_prev = np.array(x0)
        while True:
            A = calc_A(x_prev)
            F = nls(x_prev)
            z = [0.0, 0.0]
            z[1] = (F[1]*A[0][0] - A[1][0]*F[0])/(A[0][0]*A[1][1] - A[1][0]*A[0][1])
            z[0] = (F[0] - A[0][1]*z[1])/A[0][0]
            z = np.array(z)
            if np.linalg.norm(z) <= Eps:
                return x_prev - z
            x_prev = x_prev - z
            print(x_prev)


mdl = Newton()
print(mdl.run())

