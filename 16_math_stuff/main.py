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

rand1 = np.random.randn(100,1) * 10
softmax = np.exp(rand1)/np.sum(np.exp(rand1))

# plt.scatter(rand1, softmax)
# plt.show()

rand2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
logrand2 = np.log(rand2)

plt.scatter(rand2, logrand2)
plt.show()