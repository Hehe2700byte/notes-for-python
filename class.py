class Student:
    #class attributes and variables
    school = 'CUHK'
    species = 'human'
    count = 0
    #Both of the variables are regarded as class attributes. However, only the variable 'count' can be class variable.
    #class variable: a class attribute used as a shared data
    #Class attributes are shared among all instances of a class.

    #initializer(constructor)
    def __init__(self, name, age, one_pass):
        self.name = name#instance variable
        self.age = age#instance variable
        self.count += 1
        self.__one_pass = one_pass#Encapsulation: Made this information private. (Double underline)
        #Encapsulation: But if we use single leading underline, it just serves as a sign, not enforced by Python interpreter.

    #instance method: Have to use self as the first parameter
    def introduce(self):
        print(f"My name is {self.name}.")

    #Decorators built in Python
    @classmethod#Can access class variable, with first parameter cls
    def Change_School(cls, new_school):
        cls.school = new_school
    @staticmethod#Cannot access cls or self, just like normal function.
    def add(a, b):
        return a + b
    @property#The first argument is self. Attribute-like method
    def info(self):
        return self.name, self.age, self.count
    #When a property is called, there's no need to add parentheses.

    #special method: Built-in method in python
    #__init__ is just one of them
    def __str__(self):
        return f"A {self.school} student named {self.name}, age {self.age}"
    #__str__ decides how an instance was printed.
    #operator overloading
    def __add__(self, other):
        return self.age + other.age
    #__ld__, __le__, __eq__ ...

    #destructor
    def __del__(self):
        print("Successfully destructed.")
    
    
student_example1 = Student('Tom', 18)
print(student_example1)
student_example2 = Student('Tina', 19)
print(str(student_example1 + student_example2))

#inheritance
class grade(Student):
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score
        #However, if we only write like this. The constructor of parent class will not be called, neither will that of subclasses.

#Correct method:
class Tom_grade(Student):
    def __init__(self, subject, score):
        super().__init__('Tom', 18, 114514)#Have to be fixed in constructor of subclasses.

#Method overriding

class Animal:
    def __init__(self):
        pass
    def speak():
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__()
    def speak():
        print("Dog speaks")
        #If you want to use methods of parent class without modification, use: super().speak()

#Abstract Base Class
from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, r):
        super().__init__()
        self.r = r
    def area(self):
        return 3.14 * (self.r ** 2)
#One importance characteristic of ABC: The abstract methods created in superclasses have to be overridden in subclasses.

#multiple inheritance
class A:
    def f(self):
        print("A")
    

class B:
    def f(self):
        print('B')
    pass

class C(A, B):
    pass

c = C()
c.f()#What will be printed?
#python uses MRO(method resolution order): C->A->B
#Thus, A will be printed.
#diamond problem
'''
     A
    / \\
    B  C
    \\ /
      D'''
#This means that B and C are derived from A, and D is derived by B and C
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.hello()#Which A will be called?
#MRO: D->B->C->A, So A will be called only once.
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")
d = D()
#What is the output?
#Actually, in python, super means "call next class in MRO"
#SO the output will be the reverse of MRO.

#Mixin: a way of application of multiple inheritance (let base class equipped with more attributes)
class EqualityMixin:
    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)
    def __ne__(self, other):
        return not self.__eq__(other)
    
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class ComparablePoint(EqualityMixin, Point):
    pass

p = ComparablePoint(3, 4)
r = ComparablePoint(3, 2)

print(p == r)#False

#class membership test: isinstance(obj, class_name)

#polymorphism: it refers to a programming language's ability to process objects differently depending on their data type or class.
class Animal:
    def speak(self):
        pass

class Dogs(Animal):
    def speak(self):
        print("Dogs speak")

class Birds(Animal):
    def speak(self):
        print("Birds speak")

animals = [Dogs(), Birds()]
for animal in animals:
    animal.speak()
