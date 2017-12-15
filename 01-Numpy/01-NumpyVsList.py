import numpy as np
import sys

list_1 = [1,2,3,4,5,6,7,87,10,11,12,13,14,14,1,2,3,4,5,6,7,87,10,11,12,13,14,14]

np_array = np.array([1,2,3,4,5,6,7,87,10,11,12,13,14,14,1,2,3,4,5,6,7,87,10,11,12,13,14,14])

print("List takes",sys.getsizeof(list_1), "bytes")
print("Numpy takes",sys.getsizeof(np_array), "bytes")
