def add(x, y):
    print("x is {}, y is {}".format(x, y))
    return x+y

add(1, 2)#calling function

#arbitrary argument lists
def varargs(*args): #The number of inputs can not be made sure.
    return args#return a tuple

def keyword_args(**kwargs):
    return kwargs#return a dictionary

varargs(1, 2, 3)#->(1, 2, 3)
keyword_args(one = 1, two = 2)#->{"one": 1, "two": 2}

def concat(sep, *args):
    return sep.join(args)

concat("/", "a", "b", "c")#->"a/b/c"

concat("a", "b", "c")#->"bac" a is regarded as the seperator

#unpacking argument list
def sum_of_4(a, b, c, d):
    return a + b + c + d

sum_of_4(*range(2, 6))#use * to represent the unpacking argument
num_set = {"a": 1, "b": 2, "c": 3, "d": 4}
sum_of_4(*num_set)#->10(value)
sum_of_4(**num_set)#->"abcd"(key)

def all_args(*args, **kwargs):
    print(args)
    print(kwargs)

all_args(1, 2, one = 1, two = 2)#->(1, 2), {"one": 1, "two": 2}

#inner function:
def print_twins(start, end):
    assert start > 1
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
            return True
    for i in range(start, end-1):
        if is_prime(i) and is_prime(i+2):
            print(f"({i}, {i+2})")

print_twins(2, 100)

#global variable
x = 1

def set_x(num):
    x = num
    print(x)

def set_global_x(num):
    global x#use the particular variable in globle scope
    print(x)
    x = num
    print(num)

set_x(3)#->3
set_global_x(3)#->1 3

#closure
def create_avg():
    total = 0
    count = 0
    def avg(n): #for nested function, we can use "nonlocal" to use variable outside the scope of nested function
        nonlocal total, count
        total += n
        count += 1
        return total/count
    return avg#Pack total and count and store them in a specific memory. When the inner function is called again, these two values still exist.

avg = create_avg()
avg(3)#->3
avg(5)#->(3+5)/(1+1)=4

#anonymous function
(lambda x: x > 2)(3)#->true
(lambda x, y: x**2 + y**2)(1, 2)#->5

#high-order funtions
#map: y = f(x)
num = [1, 2, 3, 4]
square = map(lambda x: x**2, num)#map returns a iterator
print(list(square))
#filter:
choosen = filter(lambda x: x > 2, num)
print(list(choosen))

def add_10(num):
    num += 10
    return num

#default argument values
def func(arg = 2):
    print(str(arg))

#If we do not assign values to the function, the value of parameter will be default value.
func()#->2
func(3)#->3
#Note: The default value will only be evaluated once at the point of the definition of the function.
def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
#->
#[1]
#[1, 2]
#[1, 2, 3]
#L is a default value which is evaluated only once.

#list comprehension
[add_10(i) for i in num]#->[11, 12, 13, 14]
[x for x in num if x > 2]#->[3, 4]
#set comprehension
{x for x in "abcddeef" if x not in "abc"}#->{'d', 'e', 'f'}
#dictionary comprehension
{x: x**2 for x in range(0, 5)}#->{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#example: transpose
m = [[1, 2, 3], [1, 2, 3]]
[[x[i] for x in m] for i in range(len(m[0]))] #->[[1, 1], [2, 2], [3, 3]]
list(zip(m[0], m[1]))#->[(1, 1), (2, 2), (3, 3)]
list(zip(*m))#"*" means package
