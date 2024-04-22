import numpy as np
import matplotlib.pyplot as plt

mat1 = np.array([1,2,3,4])
mat2 = np.array([0,2,3,0])
mat3 = np.array([[1],[2],[3],[4]])

A = np.random.randn(3,5)
B = np.random.randn(5,3)

# transpose
print(mat1)
print(mat1.T)

# dot product
print(np.dot(mat1, mat2))
print(np.sum(mat1*mat2))

# matrix multiplication
print(np.matmul(mat1, mat3))
print(np.matmul(A, B))
print(A@B)

rand = np.random.randn(100,1) * 10
softmax = np.exp(rand)/np.sum(np.exp(rand))

plt.scatter(rand, softmax)
plt.show()
print(rand)