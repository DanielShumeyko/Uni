# Daniel Shumeyko \\ Applied Statistics 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math


# Create a sample and plot sample path
x = np.arange(0,20,1)
y = np.cumsum(np.random.exponential(0.5,20)) # IMPORTANT we pass inverse lambda, so if we want lambda to be 2 we pass 0.5 as the first argument

sns.set()
plt.step(x,y, c='magenta')
plt.xlabel('time')
plt.ylabel('process')
plt.suptitle('Pisson Process', fontsize=25)
plt.show()

# Here we calculate the mean value for t = 10
samples = []
for _ in range(100):
    x = np.cumsum(np.random.exponential(0.5,20))
    print(x[9])
    samples.append(x[9])
mean = np.mean(samples)
print('Mean for t=10 is ' + str(mean))
print('Program done by Daniel Shumeyko    ˙ ͜ʟ˙')

