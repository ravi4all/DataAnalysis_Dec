import numpy as np
import time

SIZE = 100000000

list_1 = range(SIZE)
# print(list_1)
list_2 = range(SIZE)

# start = time.time()

# for i in list_1:
#     for j in list_2:
#         i+j

# for i,j in zip(list_1, list_2):
#     final_list = i + j
#
# end = time.time()
# print("Total time taken",end-start)


np_array_1 = np.arange(SIZE)
np_array_2 = np.arange(SIZE)

start = time.time()

# for x in np_array_1:
#     for y in np_array_2:
#         x + y

np_array_1 + np_array_2

# for i,j in zip(np_array_1, np_array_2):
#     final_list = i + j

end = time.time()
print("Total Time by Numpy",end-start)
