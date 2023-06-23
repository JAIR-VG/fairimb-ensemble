import numpy as np
single_point = [3, 4]
points = np.arange(20).reshape((10,2))

print(points)
dist = (single_point-points)**2
print(dist)
dist = np.sum(dist, axis=1)
dist = np.sqrt(dist)
print(dist)

def mydist(vctr, mtrx):
    dist = (mtrx - vctr)**2
 #   print(dist)
    dist = np.sum(dist, axis=1)
   # dist = np.sqrt(dist)
    return np.sqrt(dist)