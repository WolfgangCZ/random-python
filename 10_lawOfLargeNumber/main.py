

import matplotlib.pyplot as plt
import numpy as np

population_size = 2.3e5
print(population_size)

population = 1/np.logspace(np.log10(0.001),np.log10(5),int(population_size))
skip = 1000

plt.plot(population[::skip], 'o')
plt.ylabel("sample")
plt.xlabel("data")

plt.show()

np.random.shuffle(population)
plt.plot(population[::skip], 'o')
