#mutable types:
#list, dictionary, set, bytearray

#list
li = []
li = [1, 2, 3]#initialization
li.append(4)#add stuff to the end of a list
print("li[-1] = "+ str(li[-1])+", "+"li[0] = "+str(li[0]))
li.pop()#remove from the end

li[0:2]#slice
li[:2]#return [1, 2]
li[0:]#return [2, 3]
li[::2]#return list selecting elements with a step size 2, [1, 3]
li[::-1]#return list in reverse order
li[1:-1:2]#li[start, end, step length]
#If you want to use the same slice over and over again, use the function slice()
x = slice(2)
li[x]#->li[0:2]
x = slice(0, 5)
li[x]#->li[0:5]
x = slice(0, 5, 2)
li[x]#->li[0:5:2]

#slice assignment
li = [1, 2, 3, 4, 5]
li[:3] = [0, 0, 0]
#li->[0, 0, 0, 4, 5]

del li[1]#delete element with index 1
li.remove(3)#remove 3 in the list

li = [1, 2, 3]
li.insert(2, 7)#insert an element at a specific index: li.insert(index, element), 2 means right behind the second element
li.index(2)#get the index of the first item matching the value
li.index(2, 0, 3)#index(value[, start[, end]])

li = [1, 2, 3]
li2 = [1, 2]
li3 = li + li2#concatenate two lists
li.extend(li2)#concatenate two lists, this method will change li.

#sortation
fruits = ['blueberry', 'papaya', 'cherry', 'lemon', 'durian', 'apple', 'banana']
fruits.sort()#change the original list directly according to initials.
fruits.sort(reverse = True)
new_fruit = sorted(fruits)#The function return a modified list, without changing the original list.
fruits.reverse()#just reverse the list no matter what initials are.

#copy
li = [1, 2, 3, 4, 5]
li1 = li
del li1[1]
li#->[1, 3, 4, 5], no new object is created.
#shallow copy(only copy the first layer of the list)
li = [1, 2, 3, 4, 5]
li1 = li[:]
li2 = list(li)
li3 = li.copy()
#deep copy(copy all layers)
import copy
li4 = copy.deepcopy(li)#This only copies list, not copies object
li = [0] * 5#li->[0, 0, 0, 0, 0]

#declare a multidimensional list
row = 2
col = 3
arr = [[0 for x in range(col)] for y in range(row)]
a = [[0] * col] * row



