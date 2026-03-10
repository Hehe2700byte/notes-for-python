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
