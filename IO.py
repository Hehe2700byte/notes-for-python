#exchange value
p = 1
q = 2
print("p= "+str(p)+" q= "+str(q))
p, q = q, p
print("p= "+str(p)+" q= "+str(q))

#judge whether a string can be an indentifier:
#s.isidentifier() and keyword.iskeyword(s), You have to "import keyword" at the start of the program.

print("Hello world", "AIST", end = '', sep = '*')#end = '' to delete '\n' automatically added, sep = '*' added * among strings.

#If you want to print \ in your code:
print(r'C:\some\name')
print('C:\\some\\name')#To use escape sequence

#string interpolation
name = 'Victoria'
code = 1001
message = "Hey, {}, your code is {}.".format(name, code)#format method
msg = "{1} {0}".format('one', 'two')#use index
print(message)
print(msg)
print(f"Hey, {name}, your code is {code}.")#f-string
print('{:<20}').format(name)#align left
print('{:>20}').format(name)#align right
print('{:^20}').format(name)#align center

#get multiple input
n, a, h = input('Please enter your name, age and height.').split()#python use split() method to split the string by space by default.
print(f"Name: {n}, Age: {a}, Height: {h}")
#eval() can automatically determine types

#integer
print(0b101)#Bin
print(0o203)#Oct
print(0x243)#Hex

# #0->convert to decimal #b->concert to binary #o->convert to octal #x->convert to hexidecimal
print(f'{0b1101:#o}')

'''For some immutable data types like int and string, if multiple variables
holding the same value are created, it is possible that only one object copy is
created in the (heap) memory for the value to optimize resources. And all
these variables are holding the memory address of that object. '''
# x = 1 y = 1, x and y hold the same id, i.e. id(x) == id(y) of x is y == true
# a = [81, 82, 83], b = [81, 82, 83], list is a mutable type. a==b but a is b == false

contents = {"aa": 21, "bb": 22}
with open("Myfile.txt","w") as file:
    file.write(str(contents)) #write a string to a file
import json

with open("Myfile.txt","w") as file:
    file.write(json.dumps(contents))#write an object to a file

with open("Myfile") as file:
    content = file.read()
print(content)#read a string from files

with open("Myfile", "r") as file:
    content = json.load(file)
#read a json object from a file