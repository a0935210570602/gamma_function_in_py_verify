import matplotlib.pyplot as plt
import math
import random
import scipy.stats as stats

def gamma_distribute(alpha,beta,t):
    sum = math.exp(-beta*t)
    for i in range(1,alpha+1):
        sum = sum*beta*t/i
    sum *= alpha/t
    return sum

beta = 0.3
alpha = 20
sigma = math.sqrt(alpha)/beta
limit = alpha/beta + 10*sigma
t = []
y = []
y_py = []
y_random = [0]*int(limit)
samples = 100000
for i in range(1, int(limit)+1):
    t.append(i)
    y.append(gamma_distribute(alpha,beta,i))
    y_py.append(stats.gamma.pdf(i, a = alpha, scale = 1/beta))
for j in range(samples):
    for i in range(int(limit)):
        if random.random() <= y[i]:
            y_random[i] += 1/samples
#plt.plot(t, y, '--')
plt.plot(t, y_py, '--')
plt.plot(t, y_random, '-')
plt.show()
