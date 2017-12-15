Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> a = [1,2,3,4,5]
>>> numpy.ndim(a)
1
>>> a2 = [[1,2],[3,4],[5,6]]
>>> numpy.ndim(a2)
2
>>> print
<built-in function print>
(
>>> print(a2)
[[1, 2], [3, 4], [5, 6]]
>>> a2[0]
[1, 2]
>>> a[0][1]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[0][1]
TypeError: 'int' object is not subscriptable
>>> a2[0][1]
2
>>> type(a2)
<class 'list'>
>>> np_array = numpy.array([1,2,3,4,5,6])
>>> np_array
array([1, 2, 3, 4, 5, 6])
>>> np_array = numpy.array([1,2,3,4,5,6,'Hi'])
>>> np_array
array(['1', '2', '3', '4', '5', '6', 'Hi'],
      dtype='<U11')
>>> np_array = numpy.array([1,2,3,4,5,6])
>>> numpy.ndim(np_array)
1
>>> np_array = numpy.array([[1,2],[3,4],[5,6]])
>>> np_array
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> numpy.ndim(np_array)
2
>>> np_array.shape
(3, 2)
>>> np_array = numpy.array([[[1,2,3],[3,4,5]],[6,7,8]])
>>> np_array
array([list([[1, 2, 3], [3, 4, 5]]), list([6, 7, 8])], dtype=object)
>>> np_array.ndim
1
>>> np_array = numpy.ndarray(1)
>>> np_array
array([ nan])
>>> np_array = numpy.ndarray([1])
>>> np_array
array([ nan])
>>> np_array = numpy.ndarray([3,5])
>>> np_array
array([[  0.00000000e+000,   7.57944724e-315,   3.90311860e-322,
                      nan,   2.36020883e-311],
       [  5.21628594e-116,   9.07638086e+223,   6.45739437e-283,
          5.29371929e+180,   1.62597455e-260],
       [  8.73990008e+245,  -1.12621825e-279,   8.06565391e-273,
          8.35428692e-308,   0.00000000e+000]])
>>> np_array = numpy.ndarray([3,1])
>>> np_array
array([[  4.24399158e-314],
       [  8.48798317e-314],
       [  1.27319747e-313]])
>>> np_array = numpy.ndarray([3,1,1])
>>> np_array
array([[[  4.24399158e-314]],

       [[  8.48798317e-314]],

       [[  1.27319747e-313]]])
>>> np_array.shape
(3, 1, 1)
>>> import numpy as np
>>> np.random.random(4)
array([ 0.99447784,  0.58184309,  0.79835702,  0.54065892])
>>> np.random.random(4) * 10
array([ 1.82629524,  8.07348047,  0.66488394,  6.2740761 ])
>>> np.random.random(4) * 100
array([ 37.02165547,  43.45807312,  50.92538363,  47.77006431])
>>> random_num = np.random.random(4) * 100
>>> print(random_num)
[ 39.57478039  88.803942    85.71238582  51.69472132]
>>> np.arange(5)
array([0, 1, 2, 3, 4])
>>> np.arange(5,5)
array([], dtype=int32)
>>> np.arange(5,15)
array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
>>> np.arange(5,15,1)
array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
>>> np.arange(5,15,2)
array([ 5,  7,  9, 11, 13])
>>> 
