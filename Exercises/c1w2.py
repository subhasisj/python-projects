import numpy as np
a = np.random.randn(2, 3) # a.shape = (2, 3)
b = np.random.randn(2, 1) # b.shape = (2, 1)
c = a + b

print(c)

a = np.random.randn(4, 3) # a.shape = (4, 3)
b = np.random.randn(3, 2) # b.shape = (3, 2)
c = a*b

a = np.random.randn(3, 3)
b = np.random.randn(3, 1)
c = a*b

print(c)