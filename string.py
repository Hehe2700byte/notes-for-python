#String is immutable. If you want to modify them, then create another string.
#You can also use methods for list in string.

#string-method
#count: count(sub[, start[, end]])
#index: index(sub[, start[, end]]) Return the index of letter first matching the substring from the left. rindex()->from the right
#find: find()/rfind() Used like index(), but return -1 when the substring is not found in the string
#replace: replace(new, old[, count]) Replace old substring with new one. Count will be used if number of replacement needs to be spicified
#strip: strip([char]), lstrip([char]), rstrip([char])
#swapcase: swapcase()
#title: title(), transform strings into the format of title
#lower/upper: lower(), upper()
#split: split(sep = char[, maxsplit = num]) num is given -1 by default, you can spicify the times of spliting
#join: join(iterable), used to formating data
ingredients = ["Eggs", "Milk", "Flour", "Sugar"]
print("Shopping list: " + ", ".join(ingredients))
print("\n".join(ingredients))
#judge: isalpha()/isalnum()/isdigit()/islower()/isupper()

