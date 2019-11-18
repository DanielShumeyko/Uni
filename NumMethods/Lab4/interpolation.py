import numpy as np

x = [-1,-1, 0, 0, 0, 1]
f = [0, 0 , 2, 2, 2, -1]
M1 = [2, 2, 4, 4, -3]
M2 = [0, 2, -2, -7]
M3 = [2, -4, -5]
M4 = [-6, -0.5]
M5 = [11/4]
M = [2.0, 0.0, 2.0, -6.0, 11/4]

def build_H():
    H = str(f[0])
    print('\n\n\n')
    for i in range(len(x)-1):
        temp = ' + ' + str(M[i])
        for j in range(i+1):
            temp += '*(x - ' + str(x[j]) + ')'
        H += temp 
    return H

def find_err(x):
    return (8*(5*x+2)/2224)*(np.absolute((x+1)^2*(x)^3*(x-1)))

print(build_H())
print('\n\n\n')
print(find_err(3))
print('\n\n\n')