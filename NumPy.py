import numpy as np

#scalar
a = np.array(1)
#1D array
b = np.array([1, 2, 3])
#2D array
c = np.array([[1, 2, 3],
             [3, 4, 5]])
'''
c.ndim -> 2
c.shape -> (2, 3)
c.size -> 6
'''

#numpy datatypes:
x = np.float64(1.0)
y = np.int_([1, 2, 3])
#modify datatype
y.astype(float)

#array creation
c = np.array([[1, 2, 3],
             [3, 4, 5]])
d = np.zeros(c.shape)#default datatype: float64
e = np.ones(c.shape)
f = np.full(c.shape, 2.2)
g = np.arange(2, 10, dtype = int)#(start, end, dtype)
#array reshaping
a = np.arange(12)
np.reshape(a, (3, 4))
#You can use arange and reshape together
np.arange(12).reshape((3, 4))
'''
->
[[0, 1, 2, 3],
[4, 5, 6, 7],
[8, 9, 10, 11]]
'''

#Sampling
'''
linspace(start, end, num, endpoint, retstep)
num: points of elements in the array
endpoint = True: The endpoint will be included.
retstep = True: A tuple containing array and step length will be returned. Otherwise, only the array will be returned.
'''
a = np.linspace(2, 8, 4, endpoint = True)#->[2, 4, 6, 8]
b = np.random.random((3, 4))
c = np.random.rand(3, 4)
d = np.random.randint(2, 10, (2,3))#(low, high, shape),[low, high),sometimes you can only give "high", and low is 0 by default.
#A more memory-efficient way:
generator = np.random.default_rng()#e is a generator
generator.random((3, 4))#[0, 1) point number
a = np.zeros((3, 4))
generator.random((3, 4), a)#Assign value to a
generator.integers(1, 10, (2, 3))#Generator.integers(low, high=None, size=None, dtype=np.int64, endpoint=False)
generator.choice(a, (2, 3))#Generator.choice(a, size = None, replace = True, p = None) If replace is False, then no duplicates.

#Basic indexing and slicing
#multidimensional matrice:
a = np.array([1, 2, 3],
             [4, 5, 6])
a[1, 2]#->6

'''When index arrays are used, what is returned is a copy of the original
data, not a view of the data as in the case for slices.'''
x = np.arange(10, 1, -1)
#x = [10, 9, 8, 7, 6, 5, 4, 3, 2]
x[[3, 3, 2, -1]]#->[7, 7, 8, 2]
x[np.array([2, 5],
           [4, 6])]
'''->[[8, 5],
      [6, 4]]'''
y = np.arange(35).reshape(5, 7)
'''array([[ 0, 1, 2, 3, 4, 5, 6],
          [ 7, 8, 9, 10, 11, 12, 13],
          [14, 15, 16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25, 26, 27],
          [28, 29, 30, 31, 32, 33, 34]])'''
y[np.array([0, 2, 4]), np.array([0, 3, 1])]
'''This slice contains (0, 0), (2, 3), (4, 1)'''
#Just like obtain the intersection
#->[0, 17, 29]
y[np.array([0, 1, 3])]
'''->[[ 0, 1, 2, 3, 4, 5, 6],
      [ 7, 8, 9, 10, 11, 12, 13],
      [21, 22, 23, 24, 25, 26, 27]]'''

''' NumPy arrays accessed using Boolean (or "mask" index) arrays.'''
a = np.arange(12).reshape(3, 4)
'''
array([[ 0, 1, 2, 3],
       [ 4, 5, 6, 7],
       [ 8, 9, 10, 11]])'''
rows_on = [True, False, True]
a[rows_on, :]#: means it takes all items on that dimension.
'''[[0, 1, 2, 3],
    [8, 9, 10, 11]]'''

b = np.arange(35).reshape(5, 7)
'''array([[ 0, 1, 2, 3, 4, 5, 6],
          [ 7, 8, 9, 10, 11, 12, 13],
          [14, 15, 16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25, 26, 27],
          [28, 29, 30, 31, 32, 33, 34]])'''
c = b > 20
'''array([[False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False],
          [True, True, True, True, True, True, True],
          [True, True, True, True, True, True, True]])'''
c[:,0]
#->[False, False, False, True, True]
b[c[:,0], :]
'''
[[21, 22, 23, 24, 25, 26, 27],
 [28, 29, 30, 31, 32, 33, 34]]])
 '''
#array operation
a = np.arange(5)
b = np.arange(5)
a + b#->[0, 2, 4, 6, 8]
a ** 2#->[0, 1, 4, 9, 16]
a > 3#->[False, False, False, False, True]
"+=, *= still work"

a = [[1, 2],
     [0, 3]]
b = [[2, 4],
     [1, 0]]

a * b = [[2, 8],
         [0, 0]]
#Actual matrix multiplication
np.dot(a, b)
'''
->
[[4, 4],
 [3, 0]]
 '''

#axis parameter
'''For a 2D array,
• axis 0 is the axis that runs vertically across the rows.
• axis 1 is the axis that runs horizontally across the columns.'''

a = np.arange(8).reshape(2, 4)
a.sum(axis = 0)
'''->[4, 6, 8, 10]'''
a.sum(axis = 1)
'''->[6, 22]'''

a = np.array([[1, 2], [3, 4]]) 
b = np.array([[5, 6]])
np.concat(a, b, axis = 0)
'''
->[[1, 2],
   [3, 4],
   [5, 6]]
'''
np.concat(a, b.T, axis = 1)
'''
->[[1, 2, 5],
   [3, 4, 6]]
'''

'''Broadcasting'''
'''In order to broadcast, the size of the trailing axes for both
arrays in an operation must either be the same size or one
of them must be one.''' 
'''From rightmost to leftmost'''

#example:
np.zeros((3, 3), int) + np.arange(3)
#trailing axis: 3 and 1
'''
->[[0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]]
   +
  [[0, 1, 2],
   [0, 1, 2],
   [0, 1, 2]]
'''

#Sorting
'''numpy.sort(a, axis=-1, kind=None, order=None)'''

#Searching
a = np.array([[100, 2, 3],[4, 5, 600]])
np.argmax(a, axis = 0)
#->[0, 1, 1]
np.argmin(a, axis = 1)
#->[1, 0]

#Counting
'''
np.any(a, axis = None)
np.all(a, axis = None)
np.not_zero(a, axis = None)'''

#image processing
from PIL import Image

im = np.array(Image.open('Sample.png'))
print(im.shape)


