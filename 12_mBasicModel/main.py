# from https://medium.com/we-are-orb/linear-regression-in-python-without-scikit-learn-50aef4b8d122

import matplotlib.pyplot as plt
import numpy as np

my_data = np.genfromtxt('12_mBasicModel/data.csv', delimiter=',') # read the data
x = my_data[:, 0].reshape(-1,1) # -1 tells numpy to figure out the dimension by itself
ones = np.ones([x.shape[0], 1]) # create an array containing only ones 
x = np.concatenate([ones, x],1) # concatenate the ones to X matrixprint(x)
y = my_data[:, 1].reshape(-1,1) # create the y matrix

plt.scatter(my_data[:, 0].reshape(-1,1), y)
# plt.show()

alpha = 0.0000001
iters = 100000
theta = np.array([[1.0, 1.0]])


def computeCost(X, y, theta):
    inner = np.power(((x @ theta.T) - y), 2) # @ means matrix multiplication of arrays. If we want to use * for multiplication we will have to convert all arrays to matrices
    return np.sum(inner) / (2 * len(x))

def gradientDescent(x, y, theta, alpha, iters):
    for i in range(iters):
        theta = theta - (alpha/len(x)) * np.sum((x @ theta.T - y) * x, axis=0)
        cost = computeCost(x, y, theta)
        if i % 10 == 0: # just look at cost every ten loops for debugging
            print(cost)
    return (theta, cost)

g, cost = gradientDescent(x, y, theta, alpha, iters)  
print(g, cost)

plt.scatter(my_data[:, 0].reshape(-1,1), y)
axes = plt.gca()
x_vals = np.array(axes.get_xlim()) 
y_vals = g[0][0] + g[0][1]* x_vals #the line equation
plt.plot(x_vals, y_vals, '--')
plt.show()