#dictionary stores mappings from keys to values

#dict creation
filled_dict = {"one": 1, "two": 2, "three": 3}
filled_dict = dict(one = 1, two = 2, three = 3)
filled_dict = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
#note: Keys of dictionary have to be immutable-type values
valid_dict = {(1, 2, 3): [1, 2, 3]}

list(filled_dict) #return list of keys of the dictinary
list(filled_dict.keys())#get a list of keys of a dictionary
list(filled_dict.values())#get a list of values of a dictionary
filled_dict['one'] = 11#assign value to the given keys

del filled_dict["one"]

"one" in filled_dict#check the existence of keys(or "not in")

#get('key'[,defaultValue])
filled_dict.get("one")#get values with corresponding keys
filled_dict.get("four")#It will return nothing, but not a error.
filled_dict.get("four", 4)#If keys do not exist, then it will return the value by default

filled_dict.items()#return dict_items([('one', 1), ('two', 2), ('three', 3)])
filled_dict.keys()#return a list of keys
filled_dict.values()#return a list of values

#pop('key'[, default value]): remove the key and return the its value. If the key is not in the dictionary, then return the default value.
filled_dict.pop('one', 1)
filled_dict.popitem()#remove and return the last inserted key-value pair 

reversed(filled_dict)#return a iterable of keys in a reversed order


d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)#merge two different dictionaries, d1 is changed. Overwrite values of the same keys.(d1 is changed)
#You can also use d1 = d1 | d2

#looping techniques
for k, v in filled_dict.items():
    print(k + ': ' + str(v))


#set
#set is mutable, frozenset is inmutable
#set creation: set(iterable), frozenset(iterable)
#set does not have indexes

s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
#set operation
s1.issubset(s2)#return a boolean value, equivalent to s1 <= s2
s1.issuperset(s2)#equivalent to s1 >= s2
s1.union(s2)#s1 is transformed into the union of s1 and s2, equivalent to s1 | s2
s1.intersection(s2)#equivalent to s1 & s2
s1.difference(s2)#equivalent to s1 - s2
s1.add(6)
s1.remove(6)

