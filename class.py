class Human:
    species = 'H.sapines' #class attribute
    def __init__(self, name): #like the constructor in C++ used to initialize an instance
        self.name = name#instance attributes
        self._age = 0#The leading undercore indicates the variable is intended to be used internally. Just for readability.
        #instance method
    def say(self, msg):#all method take "self" as the first argument
        print("{name}: {message}".format(self.name, msg))

    @classmethod#can only access class attributes
    def get_species(cls):
        return cls.species
        
    @staticmethod#called without a class or instance
    def grunt():
        return "*grunt*"
    
    @property#can access class attributes and instance attributes
    def age(self):
        return self.age
    
#inheritance
class Superhero(Human):
    #if the child class should inherit all of the parent's definitions without any modifications, you can use the keyword "pass".
    #You can also override parents' attributes
    species = 'SuperHuman'
    #child class can inherit arguments of its parents and add new arguments
    def __init__(self, name, movie = False, superpowers = ["super strength", "bulletproofing"]):
        self.fictional = True
        self.movie = movie
        self.superpowers = superpowers
        #in this case, __init__ has been overrided in the child class
        #so if you want __init__ of parent class to still be called, use function "super()"
        super().__init__(name)

    #addtional instance attributes
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}".format(pow = power))

#multiple inheritance





