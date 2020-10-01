import numpy as np

import numpy.linalg as npla

from math import sqrt

x = np.array([9, 12, 15]) # Vector

print (x.shape) # Print the shape of the vector

RS = x.reshape(3,1) # Reshape the Vector - Column Vector
print (RS) # Print the newly reshaped vector

print ("_________________________")
# Matrices
A = np.array([[2, 9, 4], [7, 6, 0]])
print (A.shape)

reshape = A.reshape(2,3)
print (reshape)
