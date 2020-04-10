# Daniel Shumeyko \\ Applied Statistics 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math


# Create a sample and plot sample path
y = np.arange(0,40,1)
x = np.cumsum(np.random.exponential(0.5,40)) # IMPORTANT we pass inverse lambda, so if we want lambda to be 2 we pass 0.5 as the first argument


print(x)


sns.set()
plt.step(x,y, c='magenta')
plt.xlabel('time')
plt.ylabel('process')
plt.suptitle('Pisson Process', fontsize=25)
plt.show()

# Here we calculate the mean value for t = 10
samples = []
for _ in range(100):
    x = np.cumsum(np.random.exponential(0.5,40))
    for i, item in enumerate(x):
        if item > 10:
            samples.append(y[i-1])



mean = np.mean(samples)
print(samples)
print('Mean for t=10 is ' + str(mean))
print('Program done by Daniel Shumeyko    ˙ ͜ʟ˙')

