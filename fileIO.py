f = open("text.txt")#open for reading(default)
f = open("text.txt", 'w')#open for writing in text mode(return the file in the form of str)
f = open("text.txt", 'r+')#read/write
f = open("text.txt", 'r + b')#read/write in binary mode

#After reading, a file should be closed
#Two methods on closing files

#1. try-finally block
f = open("text.txt", 'w')
try:
    #futher file processing
    ...
finally:
    f.close()

#2. (best method) with
with open("text.txt") as f:
    ...#further file processing

#After running the with-block, the file will be automatically closed.

#reading files
f.read()#If no size is specified, it will return all content of the file as str
f.readline()#If no size is specified, it will return a line of the file(or the rest of the line)
f.readlines()#Return all lines in list

#writing files
f.write()#write a line into files
f.writelines()#write multiple lines into files
