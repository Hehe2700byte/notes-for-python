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
e = np.random.default_rng()#e is a generator
e.random((3, 4))
a = np.zeros((3, 4))
e.random((3, 4), a)#Assign value to a
