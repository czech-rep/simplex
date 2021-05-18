import numpy as np

a = np.array([
    [1, 1, 1],
    [2, 3, 1],
    [50, 2, 2]
])

resources = np.transpose([[6, 6, 6]])
# print(resources)

diagonal = np.diag(np.ones(3))

c = np.append(a, diagonal, 1)
c = np.append(c, resources, 1)
print(c)