import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Create a sample and plot sample path
x = np.arange(0,21,1)
y = np.cumsum(np.random.exponential(2,21))

sns.set()
plt.step(x,y, c='magenta')
plt.show()

# Here we calculate the mean value for t = 10
samples = []
for _ in range(100):
    x = np.cumsum(np.random.exponential(2,21))
    samples.append(x[9])
mean = np.mean(samples)
print('Mean for t=10 is ' + str(mean))