'''
Functional Programming Paradigms: Imperative Functions/Declarative Functions

Imperative programming focuses on describing 
how a program operates or how the solution is derived.

Declarative programming is oriented around expressions 
that describe the solution rather than focus on the 
imperative approach of most procedural programming languages.

Functional programming (FP) promotes declarative programming

Avoiding side effects means not using data structures that get
updated as a program runs.
'''

#iterators
'''The built-in iter() function takes an arbitrary object and tries to
return an iterator that will return the object's contents or elements.'''
li1 = [1, 2, 3]
iterator = iter(li1)
#iterator -> <list_iterator object at 0x1014feb00>
for i in iterator:
    print(str(i))
li2 = list(iterator)
#li2 -> [1, 2, 3]
#You can create your own iterator in class
class MyCounter:
    def __init__(self, n):
        self.i = 0
        self.n = n
    
    def __iter__(self): #makes an obeject of this class iterable
        return self
    
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            return StopIteration()

counter = MyCounter(3)
print(next(counter))
print(next(counter))
print(next(counter))
try:
    print(next(counter))
except StopIteration:
    print("Iteration stopped.")
'''
Output:
0
1
2
Iteration stopped
'''

#generator
#Generator returns an iterator
#keyword: yield
'''
on reaching a yield, the generator's state of
execution is suspended; local variables are preserved. On the next call to
the generator's __next__() method, the function will resume execution.
'''
def generator_ints(n):
    for i in range(n):
        yield i#yield: 

gen = generator_ints(3)
next(gen)#->0
next(gen)#->1
next(gen)#->2

#lazy evaluation:
'''
Eager evaluation: compute everything immediately
Lazy evaluation: compute only when required
'''

#operator module
import operator
operator.add(1, 2)#->3

#itertools module
import itertools
itertools.count(1, 2)#->1, 3, 5, 7, 9, ... infinite sequence, itertools.count(start = 0, step)
itertools.cycle([1, 2, 3])#accpect an iterator and return a new iterator: 1, 2, 3, 1, 2, 3, 1, 2, 3...
itertools.repeat("abc")#->abc, abc, abc, abc... You can specify times of iteration. itertools.repeat("abc", 5)
itertools.chain((1, 2, 3), ['a', 'b', 'c'])#accept multiple iterators return a chain of them.->1, 2, 3, 'a', 'b', 'c'
itertools.islice(range(10), 8)#itertool.islice(iter, [start], end, [step])->0, 1, 2, 3, 4, 5, 6, 7
def pow(n, m):
    return n**m
itertools.starmap(pow, [(2, 3), (3, 4), (2, 4)])#itertool.starmap(func, iter)->8, 81, 16
#selecting elements
def less_than_10(n):
    if n < 10:
        return True
    else:
        return False
#We call such function "predicate"
'''returns elements for as long as
the predicate returns true. Once the predicate returns false, the
iterator will signal the end of its results.'''
itertools.takewhile(less_than_10, itertools.count())
#->0, 1, 2, 3, 4, 5, 6, 7, 8, 9
def is_even(n):
    if n % 2:
        return False
    else:
        return True
odd = itertools.filterfalse(is_even, itertools.count())#Return all the odd numbers
odd_less_than_20 = itertools.islice(odd, 10)
itertools.compress([1, 2, 3, 4, 5], [True, True, False, False, True])#Return number whose correspoding boolean is True. ->[1, 2, 5]
#Combination
itertools.combinations([1, 2, 3, 4, 5], 2)
'''
returns an iterator giving all
possible r-tuple combinations of the elements contained in iterable
'''
itertools.permutations([1, 2, 3, 4, 5], 2)#->(1, 2), (2, 1), (1, 3) ...
#Grouping elements
'''
itertools.groupby(iterable, key_func=None)
collects all the consecutive
elements from the iterable having the same key value, and returns a
stream of 2-tuples containing a key value and an iterator of those
elements with that key.
key_func is a function that can compute a key value for each element
returned by the iterable. If you don't supply a key function, the key is
simply each element itself.
'''
city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
('Anchorage', 'AK'), ('Nome', 'AK'),
('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'),
]
def city_state(city):
    return city[1]
itertools.groupby(city_list, city_state())

#higher-order functions
'''Higher order functions can accept other functions as parameters and
can return new functions as output.'''
#Python has three built-in hight-order functions
#map: map(function, iterator) -> iterator of the function
def square(n):
    return n * n
list(map(square, [1, 2, 3, 4, 5]))#->[1, 4, 9, 16, 25]

#filter:It returns an iterator from items of iterable for which function returns True.
list(is_even, range(10))#->[0, 2, 4, 6, 8]
#Reduce: Reduction is done by appyling a binary function to member in a cumulative manner. 
import functools
result = functools.reduce(operator.add, range(1, 6))#(((1+2)+3)+4)+5
