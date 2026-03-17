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

